import React from 'react';
import {Routes, Route} from 'react-router-dom';

import './App.css';
import SignInSignUpPage from './components/signInUpPage/index'
import ConfirmEmail from './components/emailPage/confirmEmail'
import SendEmail from "./components/emailPage/sendEmail";
import StartScreen from "./components/startScreen";

function App() {

    return (
        <Routes>
            <Route path='/profile' element={<StartScreen/>}/>

            <Route path='/' element={<SignInSignUpPage/>}/>
            <Route path='/email/verify/:token' element={<ConfirmEmail/>}/>
            <Route path='/email/send/' element={<SendEmail/>}/>
        </Routes>
    );
}

export default App;
