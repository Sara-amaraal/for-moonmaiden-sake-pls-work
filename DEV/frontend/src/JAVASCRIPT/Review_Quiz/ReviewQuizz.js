import React, { useState, useEffect } from 'react';
import '../../CSS/Review_Quiz/button.css'
import '../../CSS/Review_Quiz/style.css'
import '../../CSS/global.css'
import  {BoxContainerState, ContainerJustificationSubmit, AnswersContainer, Question, ButtonsAccRej} from './components';
import tab_logo from '../../IMAGES/Logo.png';
import icon from '../../IMAGES/Icon.png';
import DataFetchGet from '../../DataFetchFunctions/DataFetchGet';
import NavBar from '.././NavBar/NavBar';


let currentquestion = {};
let questions = [];



questions = [
  {
    question: "Inside which HTML element do we put the JavaScript??",
    options: ["<script>","<javascript>","<js>","<scripting>","<script href='xxx.js'>","<script name='xxx.js'>"],
    accepted: 1,
    rejected: 4
  }
];


currentquestion = questions[0];

//A react class component named 'ReviewQuizz' is created. In the class constructor, the number 
//of accepted and rejected answers, the question, the answer option and the id are defined.
//All this attributes belong to the state of the quiz. 
class ReviewQuizz extends React.Component  {
  constructor(props) {
    super(props);
    this.state = {
      accepted: 0,
      rejected: 0,
      question: "",
      options: [],
      id: 0
    }
  }
  
  //The lifecycle method 'componentWillMount' is called before the component mounts the DOM
  //so that quiz data can be fetched from the API. If the API request is successfull(payload.data.status===200)
  //then this function will set the component's state with the acquired data, while also writing
  //said data on the console. If the API request fails, the user is redirected to the homepage
  //and an alert is show on the window. 
  async componentWillMount() {
    let payload = await DataFetchGet('api/REQ4/quiz/', null);
    
    if (payload.data.status === 200) {
      console.log(payload)
      this.setState(payload);
    } else {
      window.location.href = '/';
      window.alert("There are no questions for you to review at this time.");
    }
    
  }
 
  //If the quiz's state data is not defined a div with a "Review Quizz is not avaiable" message
  //appears on the NavBar. If the quiz's state is defined its interface is rendered.
  render() {
    if(this.state.data === undefined){
      return <>
      <NavBar/>
      <div className="box pergunta" id="CreateTest_instruction">Review Quizz is not available</div>
      </>
    }else{
      return <>
      <NavBar/>
    <div className="container_geral">
          <div className="container_perguntas_respostas">
            <Question text = {this.state.data.question} />
            <div className="container_respostas">
                  <AnswersContainer option1 = {this.state.data.options[0]} 
                                    option2 = {this.state.data.options[1]}
                                    option3 = {this.state.data.options[2]}
                                    option4 = {this.state.data.options[3]}
                                    option5 = {this.state.data.options[4]}
                                    option6 = {this.state.data.options[5]}/>
            </div>
            <ButtonsAccRej/>
          </div>

        <BoxContainerState dataFromParent={{accepted: this.state.data.accepted, rejected: this.state.data.rejected, max_accepted:3}}/>
    </div>
        <ContainerJustificationSubmit id={this.state.data.id}/> 
    </>
    }
    }
  }
  
  //The ReviewQuizz component is finally exported, so it can be used in other parts of
  //the website.
  export default ReviewQuizz;
  
