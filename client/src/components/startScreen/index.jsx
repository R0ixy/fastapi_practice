import React, {useState} from 'react';

import {isSignedIn} from '../../services/authService';
import SignOut from '../signOut';
import Profile from "../profile";


function StartScreen() {

    const [isSigned, setIsSignedIn] = useState(isSignedIn());

    return (
        <>
            <Profile/>
            <SignOut isSignedIn={isSigned} onSignOut={() => setIsSignedIn(false)}/>
        </>
    );

}

export default StartScreen;