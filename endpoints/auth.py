from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from crud import user_crud
# from schemas.user import

router = APIRouter()


@router.post('/login/')
async def login(user: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = await user_crud.authenticate(db, user)
    if user is None:
        raise HTTPException(status_code=400, detail='Incorrect email or password')
    return user

# TODO make jwt authorization
