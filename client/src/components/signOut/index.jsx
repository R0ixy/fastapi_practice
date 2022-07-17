import React from 'react';
import {useNavigate} from 'react-router-dom';
import { unsetLoginSession } from "../../services/authService";
import './signOut.css';

export default function SignOut({ isSignedIn, onSignOut}) {

    const navigate = useNavigate();

    const signOut = () => {
        unsetLoginSession();
        onSignOut();
        navigate('/', {replace: true});
    }

    if(isSignedIn) {
        return (
            <div onClick={signOut} id="sign-out">Sign out</div>
        )
    }

    return null;
}