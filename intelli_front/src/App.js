import './App.css';
import Header from './components/Header'
import Landing from './pages/Landing';
import Footer from './components/Footer'
import Footer_Bar from './components/Footer_Bar';
import Login from './pages/Login'
import Signup from './pages/Signup';
import R_Main from './pages/R_Main';
import R_Candidates from './pages/R_Candidates';
import View_Profile from './pages/View_Profile';
import C_main from './pages/C_main';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Interview from './pages/Interview';
import PrivateRoute from './utils/PrivateRoute'
import { AuthProvider } from './context/AuthContext';

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
          <AuthProvider>
          <Login />
          </AuthProvider>
          </>}>
        </Route>
        <Route path="/c/signup" element={<>
          <Signup profile = {'candidate'}/>
          </>}>
        </Route>
        <Route path="/r/signup" element={<>
          <Signup profile = {'recruiter'}/>
          </>}>
        </Route>
        <Route path='/r-main' element={<PrivateRoute />}>
          
          <Route exact path = '/r-main' element = {
            <>
            <Header />
            <R_Main />
            <Footer_Bar/>
            <Footer/>
            </>
          }/>
        </Route>
        <Route path='/c-main' element={<>
          <Header />
          <C_main />
          <Footer_Bar/>
          <Footer/>
          </>}>
        </Route>
        <Route path='/interview' element={<>
          <Header />
          <Interview />
          <Footer/>
          </>}>
        </Route>
        <Route path='/r-candidates' element={<>
          <Header />
          <R_Candidates />
          <Footer_Bar/>
          <Footer/>
          </>}>
        </Route>
        <Route path='/r/view-profile' element={<>
          <Header />
          <View_Profile profile = {'recruiter'}/>
          <Footer_Bar/>
          <Footer/>
          </>}>
        </Route>
        <Route path='/c/view-profile' element={<>
          <Header />
          <View_Profile profile = {'candidate'}/>
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
