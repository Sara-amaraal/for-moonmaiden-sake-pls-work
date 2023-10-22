import React from 'react';
import Logo from '../../IMAGES/Logo.png';
import Logout from '../../IMAGES/logout.png';
import '../../CSS/NavBar/NavBar.css';
import '../../CSS/global.css';
import DataFetchGet from '../../DataFetchFunctions/DataFetchGet';

class NavBar extends React.Component {
  
    constructor() {
        super();
        this.state = {
          username: ""
        };
      }

    async componentDidMount() {
        let list_a = document.getElementById("links_nav").getElementsByTagName("a")
        let list_li=document.getElementById("links_nav").getElementsByTagName("li")
        for(let i=0;i<list_a.length;i++){
          //choose test case
          if(list_a[i].href===""){
            const aux= window.location.href.split("/")
            if(aux[aux.length-1]==="choose-test"){
              list_li[i].className="active-click"
            }
          }

          if (list_a[i].href === window.location.href){
            list_li[i].className="active-click"
          }
        }
        
        try {
          let response = await DataFetchGet('api/REQ8/get_username/', null);
         
          console.log(response);
         
          this.setState({ username: response['data'].username});
          this.setState({ status: response['data'].status});

          
        } catch (error) {
          console.log("error", error);
        }
          }

          async solve_button_action(){
            let payload = await DataFetchGet('api/REQ2/is_solver/', null);
                console.log(payload);
                if(payload.data.response === false){
                    window.alert("Must be a Solver")
                    window.location.href = "/"
                  }
                  else{
                    window.location.href = "/choose-test"
                }
          }
        

    render(){
        return<>
        <meta charset="UTF-8" />
        <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
        <title>Quirked Up Software</title>
        <link rel="stylesheet" type="text/css" href="../../CSS/NavBar/NavBar.css"/>
          
        <main>
            <header>
            <nav id="navbar">
                <div>
                    <a href="/"><img src={Logo} alt="Logo" id="logo_return_home" height="auto" width="103"/></a>
                </div>
                <ul id="links_nav">
                    <li><a href="/admin"><b>Admin</b></a></li>
                    <li><a href="/create-quizz"><b>Create Quiz</b></a></li>
                    <li><a href="/review-quizz"><b>Review Quiz</b></a></li>
                    <li><a href="/create-test"><b>Create Test</b></a></li>
                    <li><a><b onClick={this.solve_button_action}>Solve Test</b></a></li>
                    <li><a href="/profile"><b>Profile</b></a></li>
                </ul>

                <div>
                    <p id="navbar_username">{this.state.username}</p>
                </div>
                <div id="logout">
                    <a href="/login"><img src={Logout} alt="Logout" id="logout_img" height="30" width="auto"/></a>
                </div>
            </nav>
            </header>
        </main>
        </>
      }
  
}
  
export default NavBar;