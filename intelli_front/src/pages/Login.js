import { React, useContext } from 'react'
import '../styles/login.css'
import logo from '../images/intelli-logo.png'
import ir from '../images/Logo.png'
import AuthContext from '../context/AuthContext'

const Login = () => {
  let { loginUser } = useContext(AuthContext);
  return (
    <div id = "login">
      <div id = 'login-left'>
        <img src = {logo} />
      </div>
      <div id = 'login-middle'>
        <p id = "login-heading">Log In to your Account</p>
        <form onSubmit={loginUser}>
        <input type = "text" id = "login-username" placeholder='Username' name = "username"/>
        <input type = "password" id = "login-password" placeholder='Password' name = "password"/>
        <input type = "submit" id = "login-button"/>
        <p id = "login-signup">Don't have an account? <a>Sign Up</a></p>
        </form>
      </div>
      <div id = 'login-right'>
        <img src = {ir} />
      </div>
    </div>
  )
}

export default Login
