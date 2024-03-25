import {React, useState} from 'react'
import '../styles/c_main.css'
import pfp from '../images/user-image.png'
import $ from 'jquery'
import Menu from '../components/Menu'
import C_Details from './C_Details'

const C_main = () => {
  const [menu, setMenu] = useState(false);
  const [details, setView] = useState(true);
  const [buttonback, setbuttonback] = useState(false);

  const setview = () => {
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
  return (
    <>{details ? 
        <>
        <div id = 'c_bc'>
            <a onClick = {viewmenu}><img id = "c_pfp" src = {pfp} /></a>
            <div id = "c_cand"><a href = "/c-candidates">Applications History</a></div>
            <div id = "c_jl"><a href = "/c-main">Jobs List</a></div>
        </div>
        <div id = "c_main">
              <div id = "r_job">
                <pre>Software Engineer | Date</pre>
                <pre id = "r_hidden">          Views: 1000 | Applications: 1000 | Saved: 200 </pre>
                <button id = "r_vd" onClick = {setview}>View Details</button>
              </div>
              <div id = "r_job">
              <pre>Software Engineer | Date</pre>
              <pre id = "r_hidden">          Views:  | Applications:  | Saved:  </pre>
              <button id = "r_vd">View Details</button>
              </div>
              <div id = "r_job">
                <pre>Software Engineer | Date</pre>
                <pre id = "r_hidden">          Views:  | Applications:  | Saved:  </pre>
                <button id = "r_vd">View Details</button>
              </div>
              <div id = "r_job">
                <pre>Software Engineer | Date</pre>
                <pre id = "r_hidden">          Views:  | Applications:  | Saved:  </pre>
                <button id = "r_vd">View Details</button>
              </div>
              <div id = "r_job">
                <pre>Software Engineer | Date</pre>
                <pre id = "r_hidden">          Views:  | Applications:  | Saved:  </pre>
                <button id = "r_vd">View Details</button>
              </div>
              <div id = "r_job">
                <pre>Software Engineer | Date</pre>
                <pre id = "r_hidden">          Views:  | Applications:  | Saved:  </pre>
                <button id = "r_vd">View Details</button>
              </div>
        </div>
        { menu ? <><Menu /><a onClick = {viewmenu}><img id = "menu_pfp" src = {pfp} /></a></> : 
        <></>}
        </>
        :
        <>
        <C_Details company = {''} job = {''}/>
        { buttonback ? <button onClick = {setview}id = "r_main_gb"><pre>{"<< Go Back"}</pre></button> : <></>}
        { menu ? <><Menu /><a onClick = {viewmenu}><img id = "menu_pfp" src = {pfp} /></a></> : 
        <></>}
        </>
      }
      </>
  )
}

export default C_main
