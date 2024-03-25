import React from 'react'
import '../styles/interview.css'
import pfp from '../images/user-image.png'

const Interview = () => {
  return (
    <div id = "interview">
      <div id = "chatbar">
        <div id = "chathist">
            <div id = "bot">
                <img id = "botimg" src = {pfp}></img>
                <p>Bot: Hello How are you?</p>
            </div>
            <div id = "user">
                <img id = "userimg" src = {pfp}></img>
                <p>User: Hello How are you? </p>
            </div>
        </div>
        <input type = "text" id = "message" placeholder='Type your answer here...'></input>
      </div>
    </div>
  )
}

export default Interview
