import React, { useState } from 'react';
import {TextField} from '@mui/material';
import { Button } from '@mui/material'

import { createUser } from '../../services/domainRequest/userRequest';
import {useNavigate} from "react-router-dom";


export default function SignUp() {

    const [email, setEmail] = useState();
    const [password, setPassword] = useState();
    const [firstName, setFirstName] = useState();
    const [lastName, setLastName] = useState();
    const [phoneNumber, setPhoneNumber] = useState();

    const navigate = useNavigate();

    const onEmailChange = (event) => {
        setEmail(event.target.value);
    }

    const onPasswordChange = (event) => {
        setPassword(event.target.value);
    }

    const onFirstNameChange = (event) => {
        setFirstName(event.target.value);
    }

    const onLastNameChange = (event) => {
        setLastName(event.target.value);
    }

    const onPhoneNumberChange = (event) => {
        setPhoneNumber(event.target.value);
    }


    const onSubmit = async () => {
        const res = await createUser({ email, password, firstName, lastName, phoneNumber });
        if(res && res.ok) {
            const data = await res.json();
            navigate('/email/send/', {replace: true, state: {email: data.email}});
            // setLoginSession(res.json());
            // setIsLoggedIn(true);
        }

    }


    return (
        <form noValidate autoComplete="off">
            <TextField sx={{marginBottom: 1}} key="first-name" onChange={onFirstNameChange} id="standard-basic" label="First Name" placeholder="First Name"/>
            <TextField sx={{marginBottom: 1}} key="last-name" onChange={onLastNameChange} id="standard-basic" label="Last Name" placeholder="Last Name"/>
            <TextField sx={{marginBottom: 1}} key="email" onChange={onEmailChange} id="standard-basic" label="Email" placeholder="Email"/>
            <TextField sx={{marginBottom: 1}} key="phone" onChange={onPhoneNumberChange} id="standard-basic" label="Phone Number" placeholder="Phone Number"/>
            <TextField sx={{marginBottom: 1}} key="password" onChange={onPasswordChange} id="standard-basic" label="Password" placeholder="Password" type="password"/>
            <Button onClick={onSubmit} variant="contained" color="primary">Sign Up</Button>
        </form>
    )
}