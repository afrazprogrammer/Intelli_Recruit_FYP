import logo from './logo.svg';
import './App.css';
import Header from './components/Header'
import Landing from './pages/Landing';
import Footer from './components/Footer'
import Footer_Bar from './components/Footer_Bar';
import Login from './pages/Login'
import Signup from './pages/Signup';
import R_Main from './pages/R_Main';
import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
      <Routes>
        <Route path="/" element={<>
          <Header/>
          <Landing/>
          <Footer_Bar/>
          <Footer/></>}>
        </Route>
        <Route path="/login" element={<>
          <Login />
          </>}>
        </Route>
        <Route path="/signup" element={<>
          <Signup />
          </>}>
        </Route>
        <Route path='/r-main' element={<>
          <Header />
          <R_Main />
          <Footer_Bar/>
          <Footer/>
          </>}>
        </Route>
      </Routes>
    </BrowserRouter>
    </div>
  );
}

export default App;
