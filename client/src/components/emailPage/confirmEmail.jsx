import React, {useEffect, useState} from 'react';
import jwt_decode from 'jwt-decode';
import {Button, CircularProgress} from '@mui/material';
import {useNavigate, useParams} from 'react-router-dom';
import {get} from '../../services/requestHelper';
import './emailPage.css';

export default function ConfirmEmail() {

    const [data, setData] = useState({data: []});

    const {token} = useParams();
    const navigate = useNavigate();
    useEffect(() => {
        const fetchData = async () => {
            const confirmation = await get('email/verify/', token);
            setData(await confirmation.json());
        };

        fetchData();
    }, []);

    const sendNewEmail = async () => {
        const decoded = jwt_decode(token);
        const email = decoded['email'];
        await get('email/send/', email);
        navigate('/email/send/', {replace: true, state: {email: email}});
    }

    const toLogIn = () => {
        navigate('/', {replace: true})
    }

    if (!data.detail) {
        return <center><CircularProgress sx={{
            position: 'absolute',
            top: '50%'
        }}/></center>
    } else if (data && !data.detail.error) {
        return (
            <div id="container">
                <div id="wrapper">
                    <h2>Email confirmed</h2>
                    <h3>You can now sign in</h3>
                    <br/>
                    <Button variant="contained" color="primary" onClick={toLogIn}>SingIn</Button>
                </div>
            </div>
        )
    } else {
        return (
            <div id="container">
                <div id="wrapper">
                    <h2>Something went wrong</h2>
                    <h3>{data.detail.message}, please try again.</h3>
                    <br/>
                    <p>Also you can click <span id='link' onClick={sendNewEmail}>here</span> to send new email.</p>
                </div>
            </div>
        )
    }
}
