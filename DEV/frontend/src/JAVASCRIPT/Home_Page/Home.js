import React, { Component, useState, useEffect } from 'react';
import '../../CSS/Home_Page/Home.css';
import '../../CSS/global.css';
import DataFetchGet from '../../DataFetchFunctions/DataFetchGet';
import NavBar from '.././NavBar/NavBar';                          /*imports various dependencies, components including `React`, `Component`, `useState`, `useEffect` and imports CSS files for styling*/


class MyQuizzes extends Component {                               /*this component will fetch data from an API, using the `DataFetchGet` function, which depending on the response redirects to the login page or defines the data obtained in the component's state. It also has a `userQuizz` method that generates different elements depending on the `state` parameter */

    constructor(props) {
        super(props);
        this.state = {
          my_quizzes: [[[]]],
          draft_ref: "/create-quizz/"
        }
      }
    
      async componentWillMount() {
        let payload = await DataFetchGet('api/REQ2/unfinished_reproved/', null);  

        if(payload.data.unfinished_reproved_quizzes === undefined){
          console.log("going to login")
          window.location.href="/login"
        }

        this.setState({my_quizzes: payload.data.unfinished_reproved_quizzes});
        
        console.log(payload)
      }

      user_quizz(question, state, id) {

        this.draft_ref = "/create-quizz/"+id;

        if(state === 1){
          return<>
        <a href={this.draft_ref} target="_self" rel="noopener"><p className= 'MyQuizzes_quiz state_1'>State: draft<br/>Pergunta: {question}</p></a>
        </>
        }
        else if(state === 2){
          return<>
        <p className= 'MyQuizzes_quiz state_2'>State: in evaluation<br/>Pergunta: {question}</p>
        </>
        }
        else if(state === 3){
          return<>
        <a href={this.draft_ref} target="_self" rel="noopener"><p className= 'MyQuizzes_quiz state_3'>State: rejected<br/>Pergunta: {question}</p></a>
        </>
        }
        else if(state === 4){
          return<>
        <p className= 'MyQuizzes_quiz state_4'>State: accepted<br/>Pergunta: {question}</p>
        </>
        }
      }


    render(){

        return <>
        <h1 className="MyQuizzes_title">MY QUIZZES</h1>
          <div className="MyQuizzes_field">
          {this.state.my_quizzes.map(item => (
            <div className="MyQuizzes_quizz_field">
              {this.user_quizz(item[3], item[1], item[0])}
              </div>
          ))}
          </div>
        </>
    }
          
}

class HallOfFame extends Component {                     /*this component will fetch data from two API points (`api/REQ2/creators/` and `api/REQ2/solvers/`) and set it to its state */

    constructor(props) {
        super(props);
        this.state = {
          creators: [[[]]],
          solvers: [[[]]]
        }
      }

      async componentWillMount() {
        let payload_creators = await DataFetchGet('api/REQ2/creators/', null);    
        console.log(payload_creators);
        this.setState({creators: payload_creators.data.creators});

        let payload_solvers = await DataFetchGet('api/REQ2/solvers/', null);    
        console.log(payload_solvers);
        this.setState({solvers: payload_solvers.data.solvers});
      }

    render(){
    return <>
    <h1 className="HallOfFame_title">HALL OF FAME</h1>
         <div className="HOF_field" id= "HOFSolvers_field">
          <div className="HOFTitles">SOLVERS</div>
         {this.state.solvers.map(item => (
            <>
            <div className= 'HOF_user'>{item[0]} <div className= 'HOF_pontuation'>{item[1]}</div></div>
            </>
          ))}
          </div>
     
          <div className="HOF_field" id="HOFCreators_field"> 
          <div className="HOFTitles">CREATORS</div>  
          {this.state.creators.map((item) => (
            <>
            <div className= 'HOF_user'>{item[0]} <div className= 'HOF_pontuation'>{item[1]}</div></div>
            </>
          ))}
          </div>
    </> 
    }
}


class Home extends React.Component {                       /*this is the main component that renders the application, includes a navigation bar (`<NavBar />`), renders the `MyQuizzes` and `HallOfFame` components and finally defines some helper functions like `home_button`, `solve_button_action`, ` solve_button`*/

  home_button (btn_value, btn_ref, btn_type, btn_class) {

    return <a
    href={btn_ref}
    target="_self"
    rel="noopener"
    >
        <input className= {btn_class} type={btn_type} value={btn_value} id={btn_type}/> <br/>
    </a>
  }

  async solve_button_action(){
    let payload = await DataFetchGet('api/REQ2/is_solver/', null);
        console.log(payload);
        if(payload.data.response === false){
          window.alert("Must be a Solver")
        }
        else{
          window.location.href = "/choose-test"
        }
  }

  solve_button() {
    return<>
    <button className="button button_home2" id="Solve_button" value="SOLVE TEST" onClick={this.solve_button_action}>SOLVE TEST</button>
    </>
  }

    render(){
        return <>
        <main>
            <NavBar/>    
            <MyQuizzes/>
            <HallOfFame/>

          
        </main>
        </>
    }

}

export default Home;