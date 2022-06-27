from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_session
from schemas.token import TokenData
from core.config import SECRET_KEY
from core.security import ALGORITHM
from models import User
from crud import user_crud

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/users/login/token")


async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_session)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        uuid = payload.get("uuid")
        if uuid is None:
            raise credentials_exception
        token_data = TokenData(uuid=uuid)
    except JWTError:
        raise credentials_exception
    user = await user_crud.get_by_uuid(db, uuid=token_data.uuid)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    if not await user_crud.is_active(current_user):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="The user is not active")

    return current_user


async def get_current_active_superuser(current_user: User = Depends(get_current_user)) -> User:
    if not await user_crud.is_superuser(current_user):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="The user doesn't have enough privileges")

    return current_user
