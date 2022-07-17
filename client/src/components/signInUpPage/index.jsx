import React, {useState} from 'react';

import './signInUpPage.css';
import SignIn from '../signIn';
import SignUp from '../signUp';

const signPages = {
    signIn: 0,
    signUp: 1
};


function SignInSignUpPage() {
    const [index, setIndex] = useState(signPages.signIn);

    return (
        <div id="sign-in-up">
            <div id="form-wrapper">
                <div className="header">
                    <div onClick={() => setIndex(signPages.signIn)}
                         className={`${index === signPages.signIn ? 'active' : ''}`}>Sign In
                    </div>
                    <div onClick={() => setIndex(signPages.signUp)}
                         className={`${index === signPages.signUp ? 'active' : ''}`}>Sign Up
                    </div>
                </div>

                {index === signPages.signIn ? <SignIn/> : <SignUp/>}
            </div>
        </div>
    );

}


export default SignInSignUpPage;