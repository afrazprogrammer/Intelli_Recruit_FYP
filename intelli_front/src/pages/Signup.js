import React from 'react'
import '../styles/signup.css'
import logo from '../images/intelli-logo.png'
import ir from '../images/Logo.png'

const Signup = () => {
  return (
    <div id = "signup">
      <div id = 'signup-left'>
        <img src = {logo} />
      </div>
      <div id = 'signup-middle'>
        <p id = "signup-heading">Sign Up for an Account</p>
        <input type = "text" id = "signup-username" placeholder='Username'/>
        <input type = "email" id = "signup-password" placeholder='Email'/>
        <input type = "password" id = "signup-password" placeholder='Password'/>
        <input type = "submit" id = "signup-button" value={"Signup"}/>
        <p id = "signup-login">Already have an account? <a>Log In</a></p>
      </div>
      <div id = 'signup-right'>
        <img src = {ir} />
      </div>
    </div>
  )
}

export default Signup
