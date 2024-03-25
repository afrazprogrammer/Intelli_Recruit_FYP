import { React, createContext, useState } from 'react'
import { jwtDecode } from 'jwt-decode';
import { useNavigate } from 'react-router-dom';

const AuthContext = createContext()

export default AuthContext

export const AuthProvider = ({children}) => {
    const [user, setUser] = useState('');
    const [authtokens, setAuthTokens] = useState(null);
    const history = useNavigate();

    let get_type = async(e) => {
        e.preventDefault()
        let response = await fetch('http://127.0.0.1:8000/api/gettype',
            {
                method: "POST",
                headers:{
                    'Content-Type' : 'application/json'
                },
                body: JSON.stringify({"email" : user.email})
            })

            let data = await response.json();

            console.log(data);

            localStorage.setItem('type', data)

            if(data == "JobSeeker!")
            {
                history('/c-main');
            }
            else{
                history('/r-main');
            }
    }

    let loginUser = async(e) =>{
        e.preventDefault()
        console.log("Yes I am here")
        let response = await fetch('http://127.0.0.1:8000/api/token/', {
            method : 'POST',
            headers : {
                'Content-Type':'application/json',
            },
            body : JSON.stringify({'username' : e.target.username.value, 'password' : e.target.password.value})
        })
        let data = await response.json()
        if(response.status === 200){
            setAuthTokens(data.access)
            setUser(jwtDecode(data.access))
            console.log("Success")
            localStorage.setItem('user', user.username)
            localStorage.setItem('email', user.email)
            localStorage.setItem('token', authtokens)
            get_type(e)
        }
        else{

        }
    }

    let contextData = {
        loginUser : loginUser
    }

    return(
        <AuthContext.Provider value = {contextData}>
        {children}
        </AuthContext.Provider>
    )
}