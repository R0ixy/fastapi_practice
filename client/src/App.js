import React from 'react';
import {Routes, Route} from 'react-router-dom'
import Profile from './components/profile/index'
import SignInSignUpPage from './components/signInUpPage/index'
import ConfirmEmail from './components/emailPage/confirmEmail'
import SendEmail from "./components/emailPage/sendEmail";
import './App.css';

function App() {

    return (
        <Routes>
            {/*<Route path='/' element={<StartScreen/>}/>*/}
            <Route path='/' element={<SignInSignUpPage/>}/>
            <Route path='/profile' element={<Profile/>}/>
            <Route path='/email/verify/:token' element={<ConfirmEmail/>}/>
            <Route path='/email/send/' element={<SendEmail/>}/>
        </Routes>
    );
}

export default App;
