import React from 'react';
import {useLocation, useNavigate} from 'react-router-dom';
import './emailPage.css';
import {get} from "../../services/requestHelper";

export default function SendEmail() {
    const location = useLocation();
    const navigate = useNavigate();


    const sendNewEmail = async () => {
        await get('email/send/', location.state.email);
        navigate('/email/send/', {replace: true, state: {email: location.state.email}});
    }

    return (
        <div id="container">
            <div id="wrapper">
                <h2>Confirmation email was send to {location.state.email}</h2>
                <h3>Please check your email and confirm your account.</h3>
                <p>If you didn't receive an email you can <span id='link' onClick={sendNewEmail}>click here</span> to send new one.</p>
            </div>
        </div>
    )
}
