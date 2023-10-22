import React, {Component} from 'react';
import '../../CSS/Login/Login_Register.css';
import DataFetchPost from '../../DataFetchFunctions/DataFetchPost'
import DataFetchPut from '../../DataFetchFunctions/DataFetchPut';

class Header extends Component {
    constructor () {
        super()
        this.title = "Login Page"
    }
    render() {
        return(
            <header>
                <script>{window.localStorage.clear()}</script>
                <meta charSet="UTF-8" />
                <title>{this.title}</title>
                <link href={require("../../IMAGES/Icon.png")} rel="shortcut icon" type="img/png" />
                <meta content="width=device-width, initial-scale=1.0" name="viewport" />
                <link rel="stylesheet" href="../../CSS/Login_Register.css" />

                {/*---------------------------------------------LOGO---------------------------------------------*/}
                <div>
                <img src={require("../../IMAGES/Logo.png")} alt="Logo" id="logo-login" />
                </div>
            </header>
        );
    }
}

class LoginForm extends Component {
    state = {
        username: '',
        password: '',
        log: 'If you already have an account please fill these fields to login.\n',
    }

    handleUsernameInput = event => {
        this.setState({username: event.target.value})
    }
    handlePasswordInput = event => {
        this.setState({password: event.target.value})
    }
    handleLogOutput = (str) => {
        this.logRef.current.style.color = "red"
        this.setState({log: str})
    }

    
    async logValue(state){
        try{
            let a = await DataFetchPut('api/login/', {
                username: state.username,
                password: state.password
            })
            if (a.data.status !== 200){
                console.log(a.data)
                this.handleLogOutput("Invalid Credentials!")
                return
            }
            window.localStorage.setItem("token", a.data.token)
            window.location.href = '/'
        }
        catch(error){
            this.handleLogOutput("Database Unreachable!")
            console.log("database unreachable")
        }

    }

    constructor(props){
        super(props)
        this.logRef = React.createRef()
    }
    
    render() {
        return(
            <div>
                <div id="caixa-login" className="caixa-form">
                <h1 id="login-title" className="title-form">
                    <b>LOGIN</b>
                </h1>
                {/* <form id="form-login" className="formulario" onSubmit={this.handleSumit}> */}
                <div id="form-login" className="formulario">
                    <div className="texto-info">
                    <p ref = {this.logRef}>
                        {this.state.log}
                    </p>
                    </div>
                    <div className="field">
                    <label htmlFor="fullName">Username</label>
                    <input
                        type="text"
                        name="fullName"
                        id="fullName"
                        placeholder="username"
                        required="True"
                        onChange={this.handleUsernameInput}
                    />
                    </div>
                    <div className="field">
                    <label htmlFor="pass">Password</label>
                    <input
                        type="password"
                        name="pass"
                        id="pass"
                        placeholder="password"
                        minLength={6}
                        required="True"
                        onChange={this.handlePasswordInput}
                    />
                    </div>
                    {/*This is not a button, you can writte on it*/}
                    <input
                        type="submit_login"
                        id="login"
                        defaultValue="Login"
                        onClick={() => this.logValue(this.state)}
                    />
                </div>
                {/* </form> */}
                </div>
            </div>
        );
    }
    

    // handleSumit = () => {
        // var resp = DataFetchPost('api/register/', {
        //     username: username,
        //     password: password
        // })
        // return
        // e.preventDefault();

        // console.log(new FormData(e.target))

        // fetch('http://127.0.0.1:8000/api/login/', {
        //     method: 'POST',
        //     body: new FormData(e.target),
        //     credentials: 'include',
        //     mode: 'no-cors'
        // })
        // .then((res) => {
        //         console.log(res.status)
        //         if (res.status === 200) {
        //             return Promise.resolve();
        //         } else {
        //             return Promise.reject('Sign-in failed');
        //         }
        //     })
        //     .then((profile) => {
        //         // Instantiate PasswordCredential with the form
        //         if (window.PasswordCredential) {
        //             let c = new this.PasswordCredential(e.target);
        //             return navigator.credentials.store(c);
        //         } else {
        //             return Promise.resolve(profile);
        //         }
        //     })
        //     .then((profile) => {
        //         // Successful sign-in
        //         if (profile) {
        //             this.updateUI(profile);
        //         }
        //     })
        //     .catch((error) => {
        //         // Sign-in failed
        //         //this.showError('Sign-in Failed');
        //     });

    // }

    lsRememberMe = () => {
        //console.log("Register")
    }
}

class RegisterForm extends Component {
    state = {
        username: '',
        password: '',
        log: "If you don't have an account yet please register before logging in."
    }

    handleUsernameInput = event => {
        this.setState({username: event.target.value})
    }
    handlePasswordInput = event => {
        this.setState({password: event.target.value})
    }

    handleLogOutput = (str) => {
        this.logRef.current.style.color = "red"
        this.setState({log: str.trim()})
    }

    useUsernameValidation = (name) => {
        let validRegEx = "^[a-zA-Z0-9_-]+$"

        if (name.length < 6 || name.length > 18) {
            return "Username must be between 6 and 18 characters"
        }

        console.log(name.match(validRegEx))
        if (!name.match(validRegEx)) {
            return "Username must contain only alphanumerical characters, '-' and '_'"
        }
        return ""
    }

    usePasswordValidation = (pass) => {
        let validRegEx = "^[a-zA-Z0-9_\\-#$%&@]+$"

        if (pass.length < 8 || pass.length > 18) {
            return "Password must be between 8 and 18 characters"
        }

        console.log(pass.match(validRegEx))
        if (!pass.match(validRegEx)) {
            return "Password must contain only alphanumerical characters, '-', '_', '#', '$', '%', '&' and '@'"
        }
        return ""
    }
    
    async submit(state){

        const isUsernameValid = this.useUsernameValidation(this.state.username);
        const isPasswordValid = this.usePasswordValidation(this.state.password);

        if (isUsernameValid !== "" || isPasswordValid !== "") {
            this.handleLogOutput(`${isUsernameValid}\n${isPasswordValid}`);
            return
        }

        let a = await DataFetchPost('api/register/', {
            username: this.state.username,
            password: this.state.password,
        })
        console.log(a)

        if (a.data.status !== 200){
            console.log(a.data)
            if (a.data.status == 500) this.handleLogOutput("Username already exists!");
            return
        }
        
        window.localStorage.setItem("token", a.data.token)
        window.location.href = '/'
    }

    constructor(props){
        super(props)
        this.logRef = React.createRef()
    }
    render() {
        return(
            <div>
                <div id="caixa-register" className="caixa-form">
                <h1 id="register-title" className="title-form">
                    <b>REGISTER</b>
                </h1>
                <div id="form-register" className="formulario">
                    <div className="texto-info">
                    <p ref = {this.logRef}>
                        {this.state.log}
                    </p>
                    </div>
                    <div className="field">
                    <label htmlFor="username">Username</label>
                    <input
                        type="text"
                        name="fullName"
                        id="username"
                        placeholder="username"
                        required="True"
                        onChange={this.handleUsernameInput}
                    />
                    </div>
                    <div className="field">
                    <label htmlFor="password">Password</label>
                    <input
                        type="password"
                        name="pass"
                        id="password"
                        placeholder="password"
                        minLength={6}
                        required="True"
                        onChange={this.handlePasswordInput}
                    />
                    </div>
                    {/*This is not a button, you can writte on it*/}
                    <input type="submit_login" id="register" defaultValue="Register" onClick={() => this.submit(this.state)} />
                </div>
                </div>
            </div>
        );
    }
}

const Login = () => {
    return (
        <>  
            <Header/>
            <main>
                <LoginForm/>
                <div className="vl"></div>
                <RegisterForm/>
            </main>
        </>
    );
}

export default Login;
