import React, { Component, useState, useEffect } from 'react';
import '../../CSS/global.css';
import DataFetchGet from '../../DataFetchFunctions/DataFetchGet';
import '../../CSS/Profile/Profile.css';
import NavBar from '.././NavBar/NavBar';

import { BarChart, Bar, XAxis, YAxis, CartesianGrid,
  Legend, Tooltip,ResponsiveContainer } from 'recharts';


class CreatorChart extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      data:[]
    };
  }

  async componentDidMount() {
    try {
      let response = await DataFetchGet('api/REQ8/get_tags_creator/', null);
     
      console.log(response);
     
      this.setState({data: response['data'].data});
      
    } catch (error) {
      console.log("error", error);
    }
      }
 
  render(){
  if(this.state.data.length === 0){
    return (
      <>
      <div className="box pergunta" id= "profile_msg">You do not have approved or not approved quizzes!</div>
      </>
    )
  }else{
  return (
    <BarChart
      width={1500}
      height={500}
      data={this.state.data}
      layout="vertical"
      margin={{ top: 150, right: 250, bottom: 0, left: 300 }}
    >

      <text x={380} y={160} fill="black" textAnchor="middle" dominantBaseline="central" fontWeight={"bold"}>
        <tspan fontSize="18">QUIZZES</tspan></text>
      <XAxis type="number" />
      <YAxis type="category" width={40} padding={{ left: 20 }} dataKey="name" />

      <Tooltip />

      <Legend verticalAlign="top" height={36} align="right" iconSize="20" />
      <Bar name="Approved" dataKey="x" stackId="a" fill="green" />
      <Bar name="Not Approved" dataKey="y" stackId="a" fill="red" />

    </BarChart>

  );
  }}
}

class SolverChartAnswers extends React.Component{
  constructor(props) {
    super(props);
    this.state = {
      data:[],
      is_solver: 1
    };
  }

  async componentDidMount() {
    try {
      let response = await DataFetchGet('api/REQ8/get_stats_solver/', null);
      console.log(response);

      if(response.data.status === 401){
        this.setState({is_solver: 0})
      }

      this.setState({data: response['data'].data});
    } catch (error) {
      console.log("error", error);
    }
      }

  render(){
    if(this.state.is_solver === 1){
      if(this.state.data.length === 0){
        return (
          <>
          <div className="box pergunta" id= "profile_msg">You have not solved any test yet!</div>
          </>
        )
      }else{
    return (
      <BarChart
        width={1500}
        height={500}
        data={this.state.data}
        layout="vertical"
        margin={{ top: 150, right: 250, bottom: 0, left: 300 }}
      >

        <text x={385} y={160} fill="black" textAnchor="middle" dominantBaseline="central" fontWeight={"bold"}>
          <tspan fontSize="18">ANSWERS</tspan></text>
        <XAxis type="number" />
        <YAxis type="category" width={40} padding={{ left: 20 }} dataKey="name" />
  
        <Tooltip />
  
        <Legend verticalAlign="top" height={36} align="right" iconSize="20" />
        <Bar name="Correct" dataKey="x" stackId="a" fill="green" />
        <Bar name="Not Correct" dataKey="y" stackId="a" fill="red" />
  
      </BarChart>
    );}
    }else{
      return (
        <>
        <div className="box pergunta" id= "profile_msg">You must have 3 approved quizzes to become a Solver!</div>
        </>
      )
    }
  }
  
}

class Profile extends React.Component {
  
    render(){
        return <>
        <main>
          <NavBar/>    
          <CreatorChart/>
          <SolverChartAnswers/>
        </main>
        </>
    }

}

export default Profile;