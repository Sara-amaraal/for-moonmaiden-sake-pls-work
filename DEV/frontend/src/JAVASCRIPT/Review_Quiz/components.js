import '../../CSS/Review_Quiz/button.css'
import '../../CSS/Review_Quiz/style.css'
import '../../CSS/global.css'
import React from 'react'
import DataFetchPost from '../../DataFetchFunctions/DataFetchPost';

var acceptance = 2;

class ContainerJustificationSubmit extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            value: '',
            accepted: 2     // 0 for rejected, 1 for accepted, 2 is the default value
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({ value: event.target.value });
    }

    async handleSubmit (event) {
        if (acceptance === 2) {
            window.alert("You must either accept or reject the question.");
            return;
        } else if (acceptance === 0) {
            if (this.state.value.length < 40 || this.state.value.length > 512) {
                window.alert("Your justification must contain more than 40 and fewer than 512 characters.");
                return;
            }
        }
        this.state.accepted = acceptance;
        console.log(this.state);
        let data_post = JSON.stringify({
            value: this.state.value,
            accepted: acceptance,
            id: this.props.id

        });
        console.log(data_post);

        try {
            let result=await DataFetchPost('api/REQ4/vote/', data_post);
            console.log(result.data);
            window.location.href = '/';
        } catch (error) {
            console.error(error.response.data);     // NOTE - use "error.response.data` (not "error")
        }

        event.preventDefault();
    }

    render() {
        return <div className="container_justif">
            <textarea className="box justificacao" value={this.state.value} onChange={this.handleChange} placeholder="Justification of ACCEPT/REJECT" />
            <div className="container_para_botoes_submit_cancel">
                <button className = "button submit" onClick={this.handleSubmit}>SUBMIT</button>
                
                <button className = "button cancel" onClick={() => {window.location.href = '/';}}>CANCEL</button>
            </div>
        </div>
    }

}


class ButtonsAccRej extends React.Component {
    constructor() {
        super();
        this.handleSubmitAcc = this.handleSubmitAcc.bind(this);
        this.handleSubmitRej = this.handleSubmitRej.bind(this);
    }

    handleSubmitAcc (event) {
        if (acceptance === 2) {
            acceptance = 1;
            event.target.className="button accept_review_click";
        } else if (acceptance === 0) {
            acceptance = 1;
            event.target.className="button accept_review_click";
            this.reject_button.className="button reject_review";
        } else if (acceptance === 1) {
            acceptance = 2;
            event.target.className="button accept_review";
        }
        console.log(acceptance);
        
        event.preventDefault();
    }

    handleSubmitRej (event) {
        if (acceptance === 2) {
            acceptance = 0;
            event.target.className="button reject_review_click";
        } else if (acceptance === 1) {
            acceptance = 0;
            event.target.className="button reject_review_click";
            this.accept_button.className="button accept_review";
        } else if (acceptance === 0) {
            acceptance = 2;
            event.target.className="button reject_review";
        }
        console.log(acceptance);
    }

    render() {
        return <div className="container_for_button_acc_rej">
            <button className="button accept_review" ref={ref => this.accept_button = ref}  onClick={this.handleSubmitAcc}>ACCEPT</button>
            <button className="button reject_review" ref={ref => this.reject_button = ref}  onClick={this.handleSubmitRej}>REJECT</button>
        </div>
    }
}

class BoxContainerState extends React.Component {
    render() {
        return <div className="box container_estado_caixa">
            <div className="aceites">
                <p className="aceites">Accepted</p>
                <p className="aceites">{this.props.dataFromParent.accepted}/{this.props.dataFromParent.max_accepted}</p>
            </div>
            <div className="rejeitadas">
                <p className="rejeitadas">Rejected</p>
                <p className="rejeitadas">{this.props.dataFromParent.rejected}/{this.props.dataFromParent.max_accepted}</p>
            </div>
        </div>
    }
}

class Question extends React.Component {
    render() {
        return <div className="box pergunta">{this.props.text}</div>
    }
}


class ChoiceContainerReview extends React.Component {


    render() {
        //console.log(this.props.text)
        return <div className="choice-container">
            <p className={this.props.text[2] === true ? "correto choice-prefix":"choice-prefix"}>{this.props.letter}</p>
            <p className="choice-text">{this.props.text}</p>
        </div>
    }
}

class AnswersContainer extends React.Component {
    render () {
        return  <>
                    <div className="container_respostas">
                        <div id="game" className="justify-center flex-row">
                            <ChoiceContainerReview letter='A' text={this.props.option1} />
                            <ChoiceContainerReview letter='B' text={this.props.option2} />
                            <ChoiceContainerReview letter='C' text={this.props.option3} />
                            <ChoiceContainerReview letter='D' text={this.props.option4} />
                            <ChoiceContainerReview letter='E' text={this.props.option5} />
                            <ChoiceContainerReview letter='F' text={this.props.option6} />
                            </div>
                    </div>
                </>


    }

}

export {ButtonsAccRej, BoxContainerState, ContainerJustificationSubmit, ChoiceContainerReview, AnswersContainer, Question };