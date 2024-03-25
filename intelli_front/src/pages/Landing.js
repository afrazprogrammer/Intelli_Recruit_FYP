import React from 'react'
import bg1 from '../images/bg-1.png'
import bg2 from '../images/bg-2.png'
import '../styles/landing.css'
import ui from '../images/user-image.png'
import stars from '../images/star.png'

const Landing = () => {
  return (
    <div id = "landing_body">
    <a id = "landing-login" href = "/login">Login</a>
    <div id = "landing">
        <img id = 'bg1' src = {bg1}/>
        <div id = 'landing-container'>
            <div id = 'landing-left'>
                <div id = "landing-welcome-div">
                <p  id = "landing-p">Welcome to Intelli Recruit!</p>
                <p  id = "landing-p">Your Gateway to Talent Excellence!</p>
                <div id = "landing-text">
                    <p  id = "landing-p">Discover a smarter way to find top talent with Intelli Recruit. We specialize in streamlining the recruitment process, helping you connect with the most qualified candidates effortlessly.</p>
                </div>
                </div>
            </div>
            <div id = 'landing-right'>
                <a href = "/c/signup"><button id = 'dev'>Apply as Talent</button></a>
                <a href = "/r/signup"><button id = 'rec'>Apply as Recruiter</button></a>
            </div>
        </div>
    </div>
    <div id = "landing-why">
        <div id = "landing-why-head">
            <p  id = "landing-p">Why Intelli-Recruit?</p>
        </div>
        <div id = "landing-why-container">
            <div id = "lwc-left">
                <p id = "uatt">Unparalleled Access to Talent</p>
                <p  id = "landing-p">Gain access to a vast pool of skilled professionals from diverse backgrounds and industries.</p>
                <p id = "uatt">Efficient Recruitment</p>
                <p  id = "landing-p">Save time and resources with our automated interview process and candidate evaluation reports.</p>
            </div>
            <div id = "lwc-right">
                <p id = "uatt">Personalized Experience</p>
                <p  id = "landing-p">Tailor your job listings to find the perfect fit for your company culture.</p>
                <p id = "uatt">Real-time Updates</p>
                <p  id = "landing-p">Manage your job postings and candidate evaluations in one place. </p>
            </div>
        </div>
    </div>
    <div id = "landing-getting-started">
        <img id = "bg2" src = {bg2}/>
        <div id = "lgs-head">
            <p  id = "landing-p">Getting Started</p>
        </div>
        <div id = "lgs-container">
            <div id = "lgs-left">
                <p  id = "landing-p">Register Your Company</p>
                <p id = "lgs-uatt">Start by registering your company on Intelli Recruit. Provide essential details about your organization to get started.</p>
                <p  id = "landing-p">Create Job Listings</p>
                <p id = "lgs-text">Post job vacancies and customize them to match your requirements. Highlight your company's culture and values to attract top talent.</p>
            </div>
            <div id = "lgs-right">
                <p  id = "landing-p">Automatic Candidate Evaluation</p>
                <p id = "lgs-uatt">Access detailed evaluation reports, made by the AI interview bot, to make informed hiring decisions.</p>
                <p  id = "landing-p">Find Your Perfect Match</p>
                <p id = "lgs-text">Discover candidates who align with your company's vision and mission.</p>
            </div>
        </div>
    </div>
    <div id = "landing-user-reviews">
        <div id = "lur-left">
            <p id = "client-left">Here is what our clients have to say!</p>
        </div>
        <div id = "lur-right">
            <div id = 'review-container'>
                <div id = "rcl">
                    <img id = 'ui' src = {ui}/>
                    <div id = "rcl-stars">
                        <img id = "stars" src = {stars}/>
                        <img id = "stars" src = {stars}/>
                        <img id = "stars" src = {stars}/>
                        <img id = "stars" src = {stars}/>
                        <img id = "stars" src = {stars}/>
                    </div>
                </div>
                <div id = "rcr">
                    <div id = "rcr-content">"Intelli Recruit has transformed our hiring process. We were able to find the perfect candidates quickly and efficiently. The AI-driven evaluations helped us make confident hiring decisions. Highly recommended!" "Intelli Recruit has transformed our hiring process. We were able to find the perfect candidates quickly and efficiently. The AI-driven evaluations helped us make confident hiring decisions. Highly recommended!" "Intelli Recruit has transformed our hiring process. We were able to find the perfect candidates quickly and efficiently. The AI-driven evaluations helped us make confident hiring decisions. Highly recommended!" "Intelli Recruit has transformed our hiring process. We were able to find the perfect candidates quickly and efficiently. The AI-driven evaluations helped us make confident hiring decisions. Highly recommended!" "Intelli Recruit has transformed our hiring process. We were able to find the perfect candidates quickly and efficiently. The AI-driven evaluations helped us make confident hiring decisions. Highly recommended!"</div>
                </div>
            </div>
        </div>
    </div>
    </div>
  )
}

export default Landing
