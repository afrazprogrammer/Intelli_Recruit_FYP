import React from 'react'
import '../styles/login.css'
import logo from '../images/intelli-logo.png'
import ir from '../images/Logo.png'
const Login = () => {
  return (
    <div id = "login">
      <div id = 'login-left'>
        <img src = {logo} />
      </div>
      <div id = 'login-middle'>
        <p id = "login-heading">Log In to your Account</p>
        <input type = "text" id = "login-username" placeholder='Username'/>
        <input type = "password" id = "login-password" placeholder='Password'/>
        <input type = "submit" id = "login-button" value={"Login"}/>
        <p id = "login-signup">Don't have an account? <a>Sign Up</a></p>
      </div>
      <div id = 'login-right'>
        <img src = {ir} />
      </div>
    </div>
  )
}

export default Login
