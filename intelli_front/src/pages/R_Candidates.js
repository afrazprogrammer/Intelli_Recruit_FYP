import {React, useState, useEffect} from 'react'
import '../styles/r_candidates.css'
import pfp from '../images/user-image.png'
import $ from "jquery"
import View_Profile from './View_Profile'

const R_Candidates = (props) => {
    const [view_details, setviewdetails] = useState(true);
    const [data, setData] = useState('');
    
    const setview = () => {
        if(view_details === true){
            setviewdetails(false);
            $("#r_main_gb").css({"display" : "none"});
        }
        else{
            setviewdetails(true);
            $("#r_main_gb").css({"display" : "block"});
        }
        
    }

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
          setData(await response.json());
          console.log("Data", data)
    }
    
    useEffect(() => (get_company), []);
  return (
    <>
    { view_details ? <>
    <div id = 'r_bc'>
        <a href = "/login"><img id = "r_pfp" src = {pfp} /></a>
        <div id = "r_paj"><a>Post a Job</a></div>
        <div id = "r_cand"><a>Candidates</a></div>
        <div id = "r_jl"><a>Job List</a></div>
    </div>
    <div id = "r_candidates">
      <div id = "r_top">
        <p id = "r_jd">{props.job.title} Details</p>
        <p id = "r_sc">Suggested Candidates</p>
      </div>
      <div id = "r_bot">
        <div id = "r_left">
            <div id = "r_left_list">
                <ul>
                    <li><pre>Company Name:  {data.company_name}</pre></li>
                    <li><pre>Department:  {props.job.department}</pre></li>
                    <li><pre>Location:  {props.job.location}</pre></li>
                    <li><pre>Job Type:  {props.job.job_type}</pre></li>
                    <li><pre>Required Experience:  {props.job.req_exp}</pre></li>
                    <li><pre>Salary:  {props.job.salary}</pre></li>
                </ul>
            </div>
            <p id = "r_left_p">Company Description</p>
            <p id = "pre">{data.company_au}</p>
            <p id = "r_left_p">Job Description</p>
            <p id = "pre">{props.job.job_description}</p>
            <p id = "r_left_p">Key Responsibilities</p>
            <p id = "pre">{props.job.key_responsibilities}</p>
            <p id = "r_left_p">Required Skills</p>
            <p id = "pre">{props.job.required_skills}</p>
        </div>
        <div id = "r_right">
            <div id = "r_sci">
                <img src = {pfp} id = "r_candi_pfp"></img>
                <p id = "r_name">Name</p>
                <button id = "r_candi_vd" onClick = {setview}>View Details</button>
            </div>
            <div id = "r_sci">
                <img src = {pfp} id = "r_candi_pfp"></img>
                <p id = "r_name">Name</p>
                <button id = "r_candi_vd">View Details</button>
            </div>
            <div id = "r_sci">
                <img src = {pfp} id = "r_candi_pfp"></img>
                <p id = "r_name">Name</p>
                <button id = "r_candi_vd">View Details</button>
            </div>
        </div>
      </div>
    </div>
    </> :
    <>
        <div id = 'r_bc'>
            <a href = "/login"><img id = "r_pfp" src = {pfp} /></a>
            <div id = "r_paj"><a>Post a Job</a></div>
            <div id = "r_cand"><a>Candidates</a></div>
            <div id = "r_jl"><a>Job List</a></div>
        </div>
        <div id = "vd_mb">
            <button id = "vd_gb" onClick = {setview}><pre>{"<< "}Go Back</pre></button>
            <button id = "vd_d"><pre>Download Report</pre></button>
            <div id = "vd_results">
                <p>Experience Test</p>
                <progress value = {"80"} max = "100" />
                <p>{"80"}/100</p>
                <p>Technical Test</p>
                <progress value = {"80"} max = "100" />
                <p>{"80"}/100</p>
                <p>Personality Test</p>
                <progress value = {"80"} max = "100" />
                <p>{"80"}/100</p>
            </div>
        </div>
        <View_Profile profile = "candidate"/>
    </>
    }
    </>
  )
}

export default R_Candidates
