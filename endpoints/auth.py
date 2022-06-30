from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from crud import user_crud
from database import get_session
from schemas.token import Token
from core.security import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, verify_email_token, generate_email_token
from utils import send_email_task

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


@router.get('/email/send/{email}')
async def send_email(email: str, background_tasks: BackgroundTasks):
    token = generate_email_token(email)
    background_tasks.add_task(send_email_task, email, token)
    return {'Email sent'}


@router.get('/email/verify/{token}')
async def verify_email(token: str, db: AsyncSession = Depends(get_session)):
    # return dict(detail={"error": False, "message": "Success"})
    decoded = verify_email_token(token)
    if not decoded:
        raise HTTPException(status_code=400, detail={"error": True, "message": "Invalid identification token"})
    user = await user_crud.get_by_email(db, decoded['email'])
    if not user:
        raise HTTPException(status_code=404, detail={"error": True, "message": "User not found"})
    await user_crud.set_active(db, user)
    return {"detail": {"error": False, "message": "Success"}}
