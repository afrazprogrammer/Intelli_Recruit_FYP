import {React} from 'react'
import '../styles/viewprofile.css'
import pfp from '../images/user-image.png'

const View_Profile = (props) => {
    let profile = props.profile;
    console.log(props.profile)
  return (
    <>
    <div id = 'r_bc'>
        <a href = "/login"><img id = "r_pfp" src = {pfp} /></a>
        <div id = "r_paj"><a>Post a Job</a></div>
        <div id = "r_cand"><a>Candidates</a></div>
        <div id = "r_jl"><a>Job List</a></div>
    </div>
    { profile === 'candidate' ? <>
    <div id = "vp">
        <div id = "vp_top">
            <img id = "vp_pfp" src = {pfp} />
            <p id = "vp_name">Name</p>
        </div>
        <div id = "vp_left_bot">
            <ul>
                <li>Email: afraztahir123@gmail.com</li>
                <li>Phone: +923316606378</li>
                <li>Date of Birth: 05/05/2001</li>
                <li>Address: 123 Tech Avenue, San Francisco, CA 94101</li>
                <li>Profession: Software Engineer</li>
            </ul> 
            <p id = "vp_edu">Education</p>
            <ul>
                <li>Degree: </li>
                <li>Institution: </li>
                <li>Graduation Year: </li>
            </ul>
            <p id = "vp_edu">Skills</p>
            <ul>
                <li>React JS</li>
                <li>Node JS</li>
                <li>HTML/CSS</li>
            </ul>
            <p id = "vp_edu">Work Experience</p>
            <ol>
                <li>
                    <ul>
                        <li>Company Name</li>
                        <li>Title</li>
                        <li>From</li>
                        <li>Till</li>
                        <li>Description</li>
                    </ul>
                </li>
            </ol>
        </div>
    </div>
    </> : 
    <>
    <div id = "vp">
        <div id = "vp_top">
            <img id = "vp_pfp" src = {pfp} />
            <p id = "vp_name">Name</p>
        </div>
        <div id = "vp_left_bot">
            <ul>
                <li>Email: afraztahir123@gmail.com</li>
                <li>Phone: +923316606378</li>
                <li>Address: 123 Tech Avenue, San Francisco, CA 94101</li>
                <li>Established Since: 1993</li>
            </ul> 
            <p id = "vp_edu">About Us</p>
            <p id = "vp_p">Innovative Solutions Inc. is a pioneering technology company headquartered in the heart of San Francisco, California. Established in 2005, we've consistently pushed the boundaries of innovation to create cutting-edge software solutions that empower businesses to thrive in a rapidly evolving digital landscape.</p>
            <p id = "vp_edu">Our Mission</p>
            <p id = "vp_p">Our mission is simple yet profound: to harness the power of technology to solve complex challenges and drive sustainable growth for our clients. We are dedicated to delivering innovative solutions that transform industries and improve lives.</p>
            <p id = "vp_edu">Work Experience</p>
            <ul>
                <li><p id = "vp_p">Software Development: Our team of experienced engineers and developers specializes in creating custom software solutions tailored to our clients' unique requirements.</p></li>
                <li><p id = "vp_p">Consulting Services: We offer expert technology consulting services to help businesses make informed decisions and implement effective strategies.</p></li>
                <li><p id = "vp_p">AI and Machine Learning: Leveraging the latest advancements in AI and machine learning, we develop intelligent solutions that drive efficiency and innovation.</p></li>
            </ul>
        </div>
    </div>
    </>}
    </>
  )
}

export default View_Profile
