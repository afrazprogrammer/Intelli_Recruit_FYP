import {React, useState, useEffect, createContext} from 'react'
import '../styles/r_main.css'
import pfp from '../images/user-image.png'
import $ from 'jquery'
import Menu from '../components/Menu'
import R_Candidates from './R_Candidates'
import AuthContext from '../context/AuthContext'

const R_Main = () => {
  const [menu, setMenu] = useState(false);
  const [details, setView] = useState(true);
  const [buttonback, setbuttonback] = useState(false);
  const [data, setData] = useState(null);
  const [jobdata, setJobData] = useState(null);
  const [company, setCompany] = useState(null);

  const setview = (item) => {
    setJobData(item)
    if(details === true){
      setView(false);
      setbuttonback(true);
    }
    else{
      setView(true);
      setbuttonback(false);
    }
  }

  const viewmenu = () => {
    if(menu === true){
      setMenu(false);
    }
    else{
      setMenu(true);
    }
  }

  let getjobs = async() => {
    let email = localStorage.getItem('email')
    let response = await fetch('http://127.0.0.1:8000/api/r/getjoblist', {
        method: 'POST',
        headers: {
           'Content-type':'application/json'
        },
        body : JSON.stringify({"email" : email})
      })
      if (!response.ok) {
          alert(Error('Network response was not ok'));
      }
      setData(await response.json());
      get_company()

    };

    let get_company = async() => {
      let response = await fetch('http://127.0.0.1:8000/api/r/getcompany', {
          method: 'POST',
          headers: {
             'Content-type':'application/json'
          },
          body : JSON.stringify({"email" : localStorage.getItem('email')})
        })
        if (!response.ok) {
            alert(Error('Network response was not ok'));
        }
        setCompany(await response.json());
        console.log(company)
    }

    useEffect(() => getjobs, []);
  return (
    <>{details ? 
    <>
    <div id = 'r_bc'>
        <a onClick = {viewmenu}><img id = "r_pfp" src = {pfp} /></a>
        <div id = "r_paj"><a href = "/postjob">Post a Job</a></div>
        <div id = "r_cand"><a href = "/r-candidates">Candidates</a></div>
        <div id = "r_jl"><a href = "/r-main">Job List</a></div>
    </div>
    <div id = "r_main">
          {data ? (
            data.map((item, index) => (
              <div id = "r_job" key={index}>
                <pre>{item.title}</pre>
                <pre id = "r_hidden">        Views: {item.views} | Applications: {item.applied} | Saved: {item.saved} </pre>
                <button id = "r_vd" onClick = {() => {setview(item)}}>View Details</button>
              </div>
            ))
          ) : (
            <h1>No Jobs Available</h1>
          )}
    </div>
    { menu ? <><Menu /><a onClick = {viewmenu}><img id = "menu_pfp" src = {pfp} /></a></> : 
    <></>}
    </>
    :
    <>
    <R_Candidates company = {company}  job = {jobdata}/>
    { buttonback ? <button onClick = {setview}id = "r_main_gb"><pre>{"<< Go Back"}</pre></button> : <></>}
    { menu ? <><Menu /><a onClick = {viewmenu}><img id = "menu_pfp" src = {pfp} /></a></> : 
    <></>}
    </>
  }
  </>
  )
}

export default R_Main
