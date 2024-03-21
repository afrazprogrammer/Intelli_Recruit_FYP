import React from 'react'
import '../styles/r_main.css'
import pfp from '../images/user-image.png'

const R_Main = () => {
  return (
    <>
    <div id = 'r_bc'>
        <a href = "/login"><img id = "r_pfp" src = {pfp} /></a>
        <div id = "r_paj"><a>Post a Job</a></div>
        <div id = "r_cand"><a>Candidates</a></div>
        <div id = "r_jl"><a>Job List</a></div>
    </div>
    <div id = "r_main">
        <div id = "r_jpc">
            Hello Job
        </div>
    </div>
    </>
  )
}

export default R_Main
