import React, { useState } from 'react';
import { TextField } from '@mui/material';
import { Button } from '@mui/material'
import { useNavigate } from "react-router-dom";

import './signIn.css';
import { login } from '../../services/domainRequest/auth';
import { setLoginSession } from '../../services/authService';

export default function SignIn() {

    const [username, setEmail] = useState();
    const [password, setPassword] = useState();
    const navigate = useNavigate();

    const onEmailChange = (event) => {
        setEmail(event.target.value);
    }

    const onPasswordChange = (event) => {
        setPassword(event.target.value);
    }

    const onSubmit = async () => {
        const res = await login({ username, password });
        if(res && res.ok) {
            setLoginSession(await res.json());
            // setIsLoggedIn(true);

            navigate('/profile', {replace: true});
        }
    }

    return (
        <form noValidate autoComplete="off">
            <TextField sx={{marginBottom: 1}} onChange={onEmailChange} id="standard-basic" label="Email" placeholder="Email"/>
            <TextField sx={{marginBottom: 1}} onChange={onPasswordChange} id="standard-basic" label="Password" placeholder="Password" type="password"/>
            <Button onClick={onSubmit} variant="contained" color="primary">Sign In</Button>
        </form>
    )
}