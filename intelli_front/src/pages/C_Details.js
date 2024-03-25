import {React, useState} from 'react'
import '../styles/c_details.css'
import pfp from '../images/user-image.png'
import $ from "jquery"
import View_Profile from './View_Profile'
import Menu from '../components/Menu'

const C_Details = () => {
    const [view_details, setviewdetails] = useState(true);
    const [menu, setMenu] = useState(false);

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

    const viewmenu = () => {
        if(menu === true){
          setMenu(false);
        }
        else{
          setMenu(true);
        }
      }

  return (
    <>
    { view_details ? <>
    <div id = 'c_bc'>
        <a onClick = {viewmenu}><img id = "c_pfp" src = {pfp} /></a>
        <div id = "c_cand"><a href = "/c-candidates">Applications History</a></div>
        <div id = "c_jl"><a href = "/c-main">Jobs List</a></div>
    </div>
    <div id = "r_candidates">
      <div id = "r_top">
        <p id = "r_jd">Title Job Details</p>
        <p id = "r_sc">Egligibility</p>
      </div>
      <div id = "r_bot">
        <div id = "r_left">
            <div id = "r_left_list">
                <ul>
                    <li><pre>Company Name:  Atlassian</pre></li>
                    <li><pre>Department:  Atlassian</pre></li>
                    <li><pre>Location:  Atlassian</pre></li>
                    <li><pre>Job Type:  Atlassian</pre></li>
                    <li><pre>Required Experience:  Atlassian</pre></li>
                    <li><pre>Salary:  Atlassian</pre></li>
                </ul>
            </div>
            <p id = "r_left_p">Company Description</p>
            <p id = "pre">Position Overview: Innovative Solutions Inc. is seeking a talented and motivated Software Engineer to join our dynamic team in San Francisco, CA. As a Software Engineer, you will play a pivotal role in designing, developing, and maintaining cutting-edge software solutions that drive innovation and meet the needs of our clients.</p>
            <p id = "r_left_p">Job Description</p>
            <p id = "pre">Position Overview: Innovative Solutions Inc. is seeking a talented and motivated Software Engineer to join our dynamic team in San Francisco, CA. As a Software Engineer, you will play a pivotal role in designing, developing, and maintaining cutting-edge software solutions that drive innovation and meet the needs of our clients.</p>
            <p id = "r_left_p">Key Responsibilities</p>
            <p id = "pre">Position Overview: Innovative Solutions Inc. is seeking a talented and motivated Software Engineer to join our dynamic team in San Francisco, CA. As a Software Engineer, you will play a pivotal role in designing, developing, and maintaining cutting-edge software solutions that drive innovation and meet the needs of our clients.</p>
            <p id = "r_left_p">Required Skills</p>
            <p id = "pre">Position Overview: Innovative Solutions Inc. is seeking a talented and motivated Software Engineer to join our dynamic team in San Francisco, CA. As a Software Engineer, you will play a pivotal role in designing, developing, and maintaining cutting-edge software solutions that drive innovation and meet the needs of our clients.</p>
        </div>
        <div id = "c_right">
            <pre>Experience Test                                                80/100</pre>
            <progress value = "80" max = "100"></progress>
            <pre>Technical Test                                                 80/100</pre>
            <progress value = "80" max = "100"></progress>
            <pre>Personality Test                                               80/100</pre>
            <progress value = "80" max = "100"></progress>
            <pre>Skills Matched                                                 80/100</pre>
            <progress value = "80" max = "100"></progress>
            <a href = "/interview"><button id = "applyjob">Apply</button></a>
            <button id = "viewcompany" onClick={setview}>View Company Profile</button>
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
        </div>
        <View_Profile profile = "recruiter"/>
    </>
    }
    { menu ? <><Menu /><a onClick = {viewmenu}><img id = "menu_pfp" src = {pfp} /></a></> : 
    <></>}
    </>
  )
}

export default C_Details
