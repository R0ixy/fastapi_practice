from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from crud import user_crud
from database import get_session
from schemas.token import Token
from core.security import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token


router = APIRouter()


@router.post("/users/login/token", response_model=Token)
async def login_access_token(db: AsyncSession = Depends(get_session), form_data: OAuth2PasswordRequestForm = Depends()):
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = await user_crud.authenticate(
        db, email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not await user_crud.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "uuid": user.uuid,
        "access_token": create_access_token(user.uuid, expires_delta=access_token_expires),
        "token_type": "bearer",
    }
