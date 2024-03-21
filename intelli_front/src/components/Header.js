import React from 'react'
import '../styles/header.css'
import logo from '../images/intelli-logo.png'

const Header = () => {
  return (
    <div id = "header">
        <img id = "logo" src = {logo}/>
        <p id = 'intelli'>Intelli</p><p>-</p><p id = 'recruit'>Recruit</p>
    </div>
  )
}

export default Header
