import {React, useState} from 'react'
import '../styles/signup.css'
import logo from '../images/intelli-logo.png'
import ir from '../images/Logo.png'

const Signup = (props) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [email, setEmail] = useState('');

  const handleUsername = (e) => {
    setUsername(e.target.value);
  };

  const handlePassword = (e) => {
    setPassword(e.target.value);
  };

  const handleEmail = (e) => {
    setEmail(e.target.value);
  };

  const submit = async (e) => {
      e.preventDefault();
      console.log(username, password, email, props.profile);
      let response = await fetch('http://127.0.0.1:8000/api/registeruser', {
        method: 'POST',
        headers: {
           'Content-type':'application/json'
        },
        body : JSON.stringify({"username" : username, "password" : password, "email" : email, "type" : props.profile})
      })
      if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        let data = await response.json();
        console.log('Signup successful:', data);
  }

  return (
    <div id = "signup">
      <div id = 'signup-left'>
        <img src = {logo} />
      </div>
      <div id = 'signup-middle'>
        <p id = "signup-heading">Sign Up for an Account</p>
        <form onSubmit = {submit} id = "signup_form">
        <input type = "text" id = "signup-username" placeholder='Username' onChange={handleUsername}/>
        <input type = "email" id = "signup-email" placeholder='Email' onChange={handleEmail}/>
        <input type = "password" id = "signup-password" placeholder='Password' onChange={handlePassword}/>
        <input type = "submit" id = "signup-button" value={"Signup"}/>
        <p id = "signup-login">Already have an account? <a href = '/login'>Log In</a></p>
        </form>
      </div>
      <div id = 'signup-right'>
        <img src = {ir} />
      </div>
    </div>
)}

export default Signup
