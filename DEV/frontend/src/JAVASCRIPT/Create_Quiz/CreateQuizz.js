import React, { Component, useEffect, useState } from "react";
import "../../IMAGES/Logo.png";
import "../../IMAGES/Icon.png";
import "../../CSS/Create_Quiz/Create_Quizz.css";
import "../../CSS/Review_Quiz/button.css";
import "../../CSS/global.css";
import DataFetchPost from "../../DataFetchFunctions/DataFetchPost";
import DataFetchGet from "../../DataFetchFunctions/DataFetchGet";
import { useParams } from "react-router-dom";
import NavBar from '.././NavBar/NavBar';


//verification input functions
function repeatOption(listOptions) {
  if (listOptions.length<6) return;
  for (let i=0;i<listOptions.length;i++){
    for (let a=0;a<listOptions.length;a++){
      if(a!==i){
        if (listOptions[i].body===listOptions[a].body){
          alert("ERROR: Repeated answer options")
          return true;
        }
      }
    }
  }
  return false;
}
function characterInput(inputValid) {
    var characters = /[A-Za-z0-9?!.+-_,: ]+$/
    if (inputValid.match(characters)) {
    // alert("Quiz Submitted!");
    return true;}
    else if (inputValid.length===0) return true;
    else {
    alert("Please input valid characters.");
    console.log("Please input valid characters.")
    return false;
  }
}
function questao(iQuestao) {
  if(iQuestao.length===0) {
      alert('ERROR: You have to submit your question.');
      return false;
  } else {
    return true;
  }
}
function justification(explicacao) {
  if(explicacao.length===0) {
      alert('ERROR: You have to submit your justification.');
      return false;
  } else {
    return true;
  }
}
function chooseCorrect(options){
  let contador=0;
  if (options.length<6) return;
  for (let i=0;i<options.length;i++){
    if (options[i]["is_correct"]===true) contador+=1;
  }
  if(contador!==1){
    alert('ERROR: You have to choose a unique correct option')
    return false;
  }
  else return true;
}
function sixOptions(inputOption) {
  if(inputOption.length<6) {
    alert("ERROR: You have to submit six options");
    return false;
  }
  for (let i = 0; i < 6; i++) {
    if(inputOption[i].body==="") {
        alert("ERROR: You have to submit six options");
        return false;
      } 
  }
  return true;
}
async function button_save(body, options,opt_text, tag,question_id) {
  let result = await DataFetchPost("api/REQ3/save-quiz", {
      question_id: question_id,
      body: body,
      options: options,
      explanation: "explanation",
      opt_text: opt_text,
      tag:tag
  });
  console.log(result);
}
async function button_submit(body, options,opt_text, tag,question_id) {
  if(questao(body) && !repeatOption(options) && sixOptions(options) && chooseCorrect(options)) {
    let result = await DataFetchPost("api/REQ3/submit-quiz", {
      question_id: question_id,
      body: body,
      options: options,
      explanation: "",
      opt_text: opt_text,
      tag:tag
    });
    return true;
  }
  else return false;
}

const Botao = (body, options,opt_text, tag,question_id) => {
  const [state, setState] = useState({
    showMessageSaved: false,
    showMessageSubmitted: false,
  });
  function onButtonClickHandler1() {
    button_save(body, options,opt_text, tag,question_id);
    setState({ showMessageSaved: true });
  }

  function onButtonClickHandler2() {
    console.log(button_submit(body, options,opt_text, tag,question_id).then((value)=>
    {
      if(value===true){
        setState({ showMessageSubmitted: true });
        setTimeout(()=>{window.location.href = "/"},500)
      }
      else{
        setState({ showMessageSubmitted: false})
      }
    }))    
    }  
  return (
    <div>
      <h2>
        {" "}
        {state.showMessageSubmitted && <div className="alert">Quiz Submitted!</div>}
      </h2>
      <h2> {state.showMessageSaved && <div className="alert">Quiz Saved!</div>}</h2>

      <div className="container_para_botoes_save_submit_cancel">
        <div className="button-box">
          <a
            href="/" //redirect to drafts
            target="_self"
            rel="noopener"
          >
            <input className="button cancel" value="CANCEL" />
          </a>
        </div>

        <div className="button-box">
          <a
            href="/" //redirect to drafts
            target="_self"
            rel="noopener"
          >
            <input className="button submit" onClick={onButtonClickHandler1} value="SAVE" />
          </a>
        </div>

        <div className="button-box">
          {/* <a
            href="/" //redirect to drafts
            target="_self"
            rel="noopener"
          > */}
            <input
              className="button submit"
              onClick={onButtonClickHandler2}
              value="SUBMIT"
            />
          {/* </a> */}
        </div>
      </div>
    </div>
  );
};

const Question = (body, setBody) => {
  function handleQuestion(e) {
    if (characterInput(e.target.value)) {
      setBody(e.target.value);
    }
  }
  return (
    <div>
      {/*--------FIELD PARA PERGUNTA--------*/}
      <div>
        <label htmlFor="question" />
        <input className="box pergunta"
          name="question"
          id="question"
          placeholder="What's your question?"
          required=""
          value = {body}
          onChange={(e) => handleQuestion(e)}
        />
      </div>
    </div>
  );
};

const Option = (options,setOptions,id,newQuestion) => {
  const [option,setOption]=useState({id:id,body:"",is_correct:false,justification:""})
  useEffect(()=>{
      //carregar quizz
      if(newQuestion===false){
        if(options[id-1]!==undefined){
          let option_={};
          option_.id=id
          option_.body=options[id-1].body
          option_.is_correct=options[id-1].is_correct
          option_.justification=options[id-1].justification
          setOption(option_)
          options[id-1]=option_;
        }
      }
      else options[id-1]=option;
},[newQuestion,id,options])
  
  function handleChangeOption(e) {
    let option_={id:option.id,body:e.target.value,is_correct:option.is_correct,justification:option.justification}
    setOption({id:option.id,body:e.target.value,is_correct:option.is_correct,justification:option.justification})
    if (characterInput(e.target.value)) {
      let options_ = options
      options_[id - 1] = option_;
      setOptions(options_)
    } 
  }

  function checkbox(e) {
    let option_={id:option.id,body:option.body,is_correct:e.target.checked,justification:option.justification}
    setOption({id:option.id,body:option.body,is_correct:e.target.checked,justification:option.justification})
    for (let i=0;i<options.length;i++){
      if(i!==id-1){
        if(options[i].is_correct===true) options[i].is_correct=false;
      }
    }
    let options_ = options;
    options_[id - 1]=option_
    setOptions(options_);
  }

  function handleChangeJustification(e){
    let option_={id:option.id,body:option.body,is_correct:option.is_correct,justification:e.target.value}
    setOption({id:option.id,body:option.body,is_correct:option.is_correct,justification:e.target.value})
    let options_ = options
    options_[id - 1] = option_;
    setOptions(options_)
  }

  return (
    <div>
      {/*--------FIELD PARA RESPOSTA COM CHECKBOX--------*/}
      <div className="choice-container-create-quizz">
        <label htmlFor="option" />
        <input
          className="box-create-quizz"
          type="text"
          id="option"
          placeholder={`Option ${id}`}
          required=""
          value = {option.body}
          onChange={(e) => handleChangeOption(e)}
          maxLength="512"
        />
        <div className="choice-prefix-create-quizz">
          <input
            type="radio"
            name="1"
            id="check"
            required=""
            checked={option.is_correct}
            onChange={(e) => checkbox(e)}
          />
        </div>
        </div>
        <div className="justif-container-create-quizz" >
      
     {/*  <textarea className="justif-create-quizz" placeholder="Justification"></textarea> */}
      <label htmlFor="option" />
        <input
          className="box-create-quizz"
          type="text"
          placeholder={`Justification`}
          required=""
          value={option.justification}
          onChange={(e) => handleChangeJustification(e)}
          maxLength="512"
        />
        
      </div>
    </div>
  );
};

const Explanation = (opt_text,setOpt_text) => {  
  function handleExplanationInput(e) {
    if (characterInput(e.target.value)) {
      setOpt_text(e.target.value);
    }
  }
  return (
    <div className="margem">
      <div>
        <input className="box justificacao"
          name="justification"
          placeholder="Optional Text"
          required=""
          value= {opt_text}
          onChange={(e) => handleExplanationInput(e)}
        />
      </div>
    </div>
  );
};

const Explanation_Reviewer = (text) => {  
  return (
    <div className="margem">
      <div>
        <input className="box justificacao"
          name="justification"
          placeholder="Reviewer Justification"
          required=""
          value= {text}
        />
      </div>
    </div>
  );
};


const Tags = (tag,setTag)=>{
  const [tags,setTags]=useState([])
  useEffect(()=>{
    async function a (){
      try {
        //buscar tags
        const response = await DataFetchGet('api/REQ6/tags/', null);
        let tags_=response.data.tags;
        if(tags_.length===0){
          setTags(["-1"])
          setTag("-1")
        }
        else {setTags(tags_);setTag(tags_[0]);}
    } catch (error) {
        setTags(["-1"])
        setTag("-1")
    }}
    a();
  },[setTag])
  function tagHandler(e){
    setTag(e.target.value);
  }
  return (
    <div className='menu-trigger'>
          <div className="dropdown">
            <label className ="choose-tag" for="tags">Choose tag</label>
            <select name="tags" id="tags" value={tag} onChange={e=>{tagHandler(e)}}>
            {tags.map(item=>{
                return (<option value={item}>{item}</option>)
            })}
            </select>
          </div>
        </div>
  )
}
const CreateQuizz = () => {
  const id = parseInt(useParams().id);
  const [reviewJustifications,setReviewJustifications]=useState([])
  const [body, setBody] = useState("");
  const [options, setOptions] = useState([]);
  const [opt_text, setOpt_text] = useState("");
  const [question_id, setQuestion_id] = useState(0);
  const [tag,setTag]=useState("");
  const [newQuestion,setNewQuestion]=useState(true);

  useEffect(()=>{
    if(isNaN(id))console.log("New Quizz")
    else {
      console.log("Quizz Existente")
      let result = DataFetchGet(`api/REQ3/get-quiz/${id}`).then((value)=>{
        let data = value["data"]["data"]
        if (value.success==="no"){
          alert("ERROR: DataBase is not connected");
          setTimeout(()=>{window.location.href = "/"},1000)
        }
        else if (data.status===404) {
          alert(`ERROR: ${data["message"]}`)
          setTimeout(()=>{window.location.href = "/"},1000)
        }
        
        else if (value.success==="yes"){
          console.log(data)
          setOptions(data.options)
          setBody(data.question)
          setTag(data.tag)
          setOpt_text(data.opt_text)
          setQuestion_id(id)
          setNewQuestion(false)
          setReviewJustifications(data.rejected_justifications);
        }
        })
        }
},[id])

  return (
    <div>
      <NavBar/>
      {Tags(tag,setTag)}
      {Question(body,setBody)}
      {Explanation(opt_text,setOpt_text)}
      <div className="grid-container">
        {Option(options,setOptions,1,newQuestion)}
        {Option(options,setOptions,2,newQuestion)}
        {Option(options,setOptions,3,newQuestion)}
        {Option(options,setOptions,4,newQuestion)}
        {Option(options,setOptions,5,newQuestion)}
        {Option(options,setOptions,6,newQuestion)}
      </div>
      {reviewJustifications.length>0 && <h2>Review Justifications</h2>}
      {reviewJustifications.length>0  && reviewJustifications.map((item)=>{
        return Explanation_Reviewer(item.justification)})}
      {Botao(body, options,opt_text, tag,question_id)}
    </div>
  );
};
export default CreateQuizz;