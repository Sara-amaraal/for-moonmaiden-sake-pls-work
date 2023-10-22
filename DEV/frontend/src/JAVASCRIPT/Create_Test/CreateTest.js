import '../../CSS/global.css';
import '../../CSS/Review_Quiz/button.css';
import '../../CSS/Create_Test/style_tags.css';
import React from 'react'
import DataFetchPost from '../../DataFetchFunctions/DataFetchPost';
import DataFetchGet from "../../DataFetchFunctions/DataFetchGet";
import NavBar from '.././NavBar/NavBar';

  
class CreateTest extends React.Component {
  constructor(props) {  //initial constructor 
    super(props); 
    this.state = {
      title: '',
      tags: [],
      get: {}
    };

    this.handleTitleChange = this.handleTitleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  async componentDidMount() {
    try {
      const response = await DataFetchGet('api/REQ6/tags/', null); //fetches data form REQ6Q
      console.log(response);
      this.setState({
        title: this.state.title,
        tags: this.state.tags,
        get: response
      });
    } catch (error) {
      console.log("error", error);
    }
  }

  async handleSubmit(event) { //when the SUBMIT button is clicked
    if (this.state.tags.length !== 2) { 
      window.alert("You must select 2 tags."); //checks if the user selected 2 tags
    } else if (this.state.title.length < 10) {
      window.alert("The test must have a title with at least 10 characters."); //checks if the title is at least 10 characters
    } else {
      console.log(this.state);

      let data_post_create_test = JSON.stringify({ //if conditions are right, send request to api/REQ6/test with the test data
        title: this.state.title,
        tags: this.state.tags
      });
      console.log(data_post_create_test);

      try {
        let result=await DataFetchPost('api/REQ6/test/', data_post_create_test);
        console.log(result);
        if (result.data.status === 400) {
          window.alert("Cannot create test; " + result.data.errors);
        }
        else {
          let tagtext = "";
          console.log(result.data.count);
          /*
          * {
          * 'PM': 5
          * 'REQ': 5
          * }
          *
          * */
          for (const key in result.data.count) {
            tagtext += result.data.count[key] + ' X ' + key + ';\n';
          }
          tagtext = tagtext.slice(0, tagtext.length - 2);
          window.alert('Test created successfully! \n' + tagtext);
        }
        window.location.href = '/';
      } catch (error) {
        console.error(error.response.data);     // NOTE - use "error.response.data` (not "error")
      }
    }
    
    event.preventDefault();
  }

  handleTitleChange(event) { //updates title
    this.setState({
      title: event.target.value,
      tags: this.state.tags,
      get: this.state.get
    });
    event.preventDefault();
  }

  handleTagButtonClick (tagName) { //add or remove tags
    const existsTag = (element) => element === tagName;
    let tagIndex = this.state.tags.findIndex(existsTag);
    if (tagIndex === -1) { 
      this.state.tags.push(tagName);
    } else {
      this.state.tags.splice(tagIndex, 1);
    }
    console.log(this.state);
  }
  

  render() { //shows content based on the get.data property
       if(this.state.get.data === undefined) {
         return <>
         <NavBar/>
         <div className="box pergunta" id="CreateTest_instruction">Create Test is not available</div>
         </>
    } else return <>
      <NavBar/>
      <div className="box pergunta" id="CreateTest_instruction">Choose a title for the test and select 2 tags.</div>
      <textarea className="box pergunta" id= "test_title_box" value={this.state.title} onChange={this.handleTitleChange} placeholder='Title:' />

      <div className="container_tags">


        {this.state.get.data.tags.map((name, key) => {
          return (
            <div key={key}>
              <ButtonTag name={name} onClick={() => this.handleTagButtonClick(name)}/>
            </div>
          );
        })}

      </div>
      <div className="container_submit_cancel_tags">
        <button className="button submit" onClick={this.handleSubmit}>SUBMIT</button>
        <button className="button cancel" onClick={() => { window.location.href = '/'; }}>CANCEL</button>
      </div>
      {"}"}
    </>
  }
}

const ButtonTag = ({ name, onClick }) => { //button form selecting tags
    function handleClick(e) {
      onClick();
      if(e.target.className === "button tag_button") e.target.className="button tag_button_click";
      else e.target.className="button tag_button";
    };
  
  return < button onClick={e=>{handleClick(e)}} className="button tag_button">{name} </button>;
}



export default CreateTest;

