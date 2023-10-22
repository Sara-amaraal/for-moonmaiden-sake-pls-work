import React, { Component, useState, useEffect } from 'react';
import '../../CSS/global.css';
import DataFetchGet from '../../DataFetchFunctions/DataFetchGet';
import '../../CSS/Choose_Test/ChooseTest.css';
import NavBar from '.././NavBar/NavBar';

class TestList extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      tests_to_solve: [[[]]]
    }
  }

  async componentDidMount() {
    let payload = await DataFetchGet('api/REQ5/choose-test/', null);  
    console.log(payload);
    this.setState({tests_to_solve: payload.data.tests});
    if (this.state.tests_to_solve.length === 0) {
      window.alert("You have no tests to solve!");
      window.location.href = "..";
    }
  }

  async test_chosen_action(test_id) {
    window.location.href = `/solve-test/` + test_id;
  }

  render(){
    return <>
      {this.state.tests_to_solve.map((item) => (
            <>
            <div onClick={() => this.test_chosen_action(item['id'])} className="box chooseTest_box">
                <b>{item['title']}</b><br/>
              {item['tags']?.map((item2) => (
                <div className="ChooseTest_tag">
                  <p>{item2}</p>
                </div>
              ))}
            </div>
            </>
          ))}
    </>
  }
}

class ChooseTest extends React.Component { 
      render(){
          return <>
          <main>
            <NavBar/>
            <TestList/>
          </main>
          </>
      }
  }
  
  export default ChooseTest;