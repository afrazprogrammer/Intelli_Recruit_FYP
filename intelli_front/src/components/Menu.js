import React from 'react'
import "../styles/menu.css"

const Menu = () => {
  return (
    <div id = "menu">
      <p id = "menu_name">Name</p>
      <a><p id = "menu_a">View Profile</p></a>
      <br></br>
      <br></br>
      <br></br>
      <a><p id = "menu_a">Edit Profile</p></a>
      <br></br>
      <br></br>
      <br></br>
      <a><p id = "menu_a">Logout</p></a>
    </div>
  )
}

export default Menu