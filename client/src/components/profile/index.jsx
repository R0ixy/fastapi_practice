import React, {useEffect, useState} from 'react';
import jwt_decode from 'jwt-decode';
import {getUser} from "../../services/domainRequest/userRequest";
import {getCurrentUser} from "../../services/authService";

import './profile.css'
import {Button, CircularProgress, IconButton} from "@mui/material";
import PhotoCamera from '@mui/icons-material/PhotoCamera';


function Profile() {
    const [user, setUser] = useState(null);
    const [visibility, setVisibility] = useState({visibility: 'hidden'});

    useEffect(() => {

        const current_user = getCurrentUser();
        const decoded = jwt_decode(current_user['access_token']);
        async function fetchData() {
            const user_info = await getUser(decoded['uuid'], current_user['access_token']);

            if (user_info && !user_info.error) {
                return await user_info.json();
            }
        }
        fetchData().then(data => {setUser(data)});
    }, []);

    const showPhotoButton = () => {
        setVisibility({visibility: 'visible'});
    }

    const hidePhotoButton = () => {
        setVisibility({visibility: 'hidden'});
    }


    if (!user) {
        return (<center>
                <CircularProgress sx={{
                    position: 'absolute',
                    top: '50%'
                }}/>
            </center>
        )
    } else {


        return (
            <div className="profile-container">
                <div className="card">
                    <div className="card-content">
                        <div className="image" onMouseEnter={showPhotoButton} onMouseLeave={hidePhotoButton}>
                            {/*<img src="https://i.imgur.com/toJNI1l.jpg" alt='user avatar'/>*/}
                            <IconButton color="primary" aria-label="upload picture" component="span">
                                <img
                                    src="http://images2.minutemediacdn.com/image/upload/c_crop,h_1193,w_2121,x_0,y_64/f_auto,q_auto,w_1100/v1565279671/shape/mentalfloss/578211-gettyimages-542930526.jpg"
                                    alt='user avatar'/>
                                <PhotoCamera style={visibility} className='photoButton'/>
                            </IconButton>
                        </div>
                        <div className="text-center">
                            <h2>{user.firstName} {user.lastName}</h2>
                        </div>
                        <div className="stats">
                            <div className="stat1">
                                <span>132</span>
                                <span>Followers</span>
                            </div>
                            <div className="stat1">
                                <span>16</span>
                                <span>Posts</span>
                            </div>
                            <div className="stat1">
                                <span>20</span>
                                <span>Follows</span>
                            </div>
                        </div>
                        <div className="buttons">
                            <Button className="follow" variant="contained">Follow</Button>
                            <Button className="message">Message</Button>
                        </div>
                    </div>
                </div>
            </div>
        )
    }

}

export default Profile;