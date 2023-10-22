import React from 'react';
import '../../CSS/global.css'
import '../../CSS/Solve_Test/SolveTest.css'
import DataFetchGet from '../../DataFetchFunctions/DataFetchGet';
import DataFetchPost from '../../DataFetchFunctions/DataFetchPost';
import NavBar from '.././NavBar/NavBar';


var global = {}; //guarda info global relacionada ao quiz
var grade_results = {}; //guarda os resultados do teste
var submitted = false; //verificação se o quiz foi bem submetido

class Option extends React.Component {
    constructor() {
        super();
        this.option_classname = this.option_classname.bind(this);
    }
    
    handleClick() {
        //console.log("selected " + this.props.data.id + " in question " + this.props.id);
        global.solutions[this.props.id] = this.props.data.id;  //update a opção selecionada
    }
    
    //TESTE CORRETO OU ERRADO

    option_classname() {
        let ret = "choice-prefix ";
        if (submitted === true) {
            if (this.props.data.id === grade_results.results[this.props.id].correct) {
                ret += "solve_test_correto";
            } else if (this.props.data.id !== grade_results.results[this.props.id].correct) {
                if (Object.values(global['solutions']).indexOf(this.props.data.id) > -1) { // checka se o id do item é encontrado
                    ret += "solve_test_errado";    
                }
            }
        }
        return ret;
    }

    render() {
        return <div className="choice-container ">
            <div className={this.option_classname()}>
                <input type="radio" name={this.props.id} id="answer" value="answer" onClick={() => this.handleClick()} />
            </div>
            <div className="choice-text">{this.props.data.body}</div>

        </div>
    }
}

//renderização de uma questão
//opcionalmente, se o quiz foi devidamente submetido e se há resultados disponíveis

class Quiz extends React.Component {
    render() {
        return (
            <>
                <div className="box pergunta">{this.props.data.body}</div>
                <div className={"container_solve_test_options"}>
                {this.props.data.opts.map(opts => (
                        <Option data={opts} id={this.props.data.id} key={opts.id} />
                ))
                }
                </div>
                {(submitted === true && this.props.data.id in grade_results.results) && <div className="box pergunta" id="justification_box" >Justification: {grade_results.results[this.props.data.id].justification}</div>}
            </>
        );
    }
}

//botoes para interagir com o quiz, (submeter respostas, navegar na interface)

class Buttons extends React.Component {
    constructor() {
        super();
        this.handleSubmit = this.handleSubmit.bind(this);
    }


    async handleSubmit(event) {
        let data_post = JSON.stringify(global);
        // console.log(data_post);

        await DataFetchPost(`api/REQ5/grade_test/`, data_post
        ).then((result) => {
            let data = result.data
            if (data['status'] === 501) {
                console.log(data['log']);
                window.alert("You've already done this test!");
                window.location.href = "..";
                return;
            } else if (data['status'] === 500) {
                window.location.href = "/login";
                window.alert(data['log']);
                return;
            }

            console.log(result);
            //console.log(data);
            grade_results = data;
            window.scrollTo(0, 0);
            submitted = true;
            //console.log(JSON.stringify(grade_results));
            this.props.rerender();
            },
        );

        event.preventDefault();
    }

    async handleCancel(event) {
        if (window.confirm("Are you sure you want to go to homepage?")) {
            window.location.href = '..';
        }
        event.preventDefault();
    }

    render() {
        return <div className="container_solve_test_buttons">
            {submitted === false &&  <button className="button" onClick={this.handleSubmit}>SUBMIT</button>} 
            {submitted === true && <button className="button">YOU GOT {grade_results.grade} POINTS</button>}
            {submitted === false && <button className="button" onClick={this.handleCancel}>CANCEL</button>}
            {submitted === true && <button className="button" onClick={this.handleCancel}>HOMEPAGE</button>}
        </div>
    }
}

//disposição da interface na resolução de testes

class SolveTest extends React.Component {
    constructor(props) {
        super(props);

        // exemplo - não retirar
        this.state = {
            questions: [
                {
                    id: "1",
                    body: "ola",
                    opts: [
                        { id: 1, body: "opta1" }
                    ]
                }
            ]
        }
        this.rerender = this.rerender.bind(this);
    }

    rerender() {
        this.setState(this.state);
    }
    
    async componentDidMount() {
        let currentUrl = JSON.stringify(window.location.href);
        let lastSlash = currentUrl.lastIndexOf("/");
        let test_id = currentUrl.slice(lastSlash+1, -1);
        test_id = parseInt(test_id);
        let temp = { "id": test_id };
        
        await DataFetchGet(`api/REQ5/get_test/`, temp
        ).then((result) => {
            let data = result.data
            if (data['status'] === 401) {
                console.log(data['log']);
                return;
            } else if (data['status'] === 500) {
                window.location.href = "/login";
                window.alert(data['log']);
                return;
            }
            global = temp;
            let solutions = {};
            for (let i = 0; i < result.data.questions.length; i++) {
                solutions[result.data.questions[i].id] = -1;

            }
            global["solutions"] = solutions;
            
            //console.log(global); 
            //console.log(result);
            this.setState(result.data);
            },
        );
    }
    
    render() {
        return <>
            <main>
                <NavBar/>
                <div className="container_solve_test">
                    {this.state.questions.map(quiz => {
                        return (
                            <Quiz data={quiz} key={quiz.id}></Quiz>
                        );
                    })}
                    <Buttons rerender={this.rerender}></Buttons>
                </div>
            </main>
        </>
    }
}


export default SolveTest;