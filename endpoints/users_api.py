from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession

from crud import user_crud
from schemas.user import UserCreate, User
import models
from database import get_session
from .deps import get_current_active_user
from utils import send_email_task
from core.security import generate_email_token
router = APIRouter()


@router.get('/', response_model=list[User])
async def get_many_users(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_session)):
    """Get many user entries from the database

    * `skip`: Number of entries to skip
    * `limit`: Maximum number of entries to return
    """

    return await user_crud.get_many(db, skip, limit)


@router.get('/{uuid}', response_model=User)
async def get_one_user(
        uuid: str,
        db: AsyncSession = Depends(get_session),
        current_user: models.User = Depends(get_current_active_user)
):
    """Get one user entry from database by uuid

    * `uuid`: User uuid
    """

    return await user_crud.get_by_uuid(db, uuid)


@router.post('/', response_model=User)
async def create_user(user: UserCreate, background_tasks: BackgroundTasks, db: AsyncSession = Depends(get_session)):
    """Create new user in database"""

    db_user_by_email = await user_crud.get_by_email(db, user.email)
    if db_user_by_email:
        raise HTTPException(status_code=400, detail='Email is already registered')

    db_user_by_phone = await user_crud.get_by_phone(db, user.phoneNumber)
    if db_user_by_phone:
        raise HTTPException(status_code=400, detail='Phone number is already registered')

    token = generate_email_token(user.email)
    background_tasks.add_task(send_email_task, user.email, token)
    return await user_crud.create_new(db, user)


@router.delete('/{uuid}')
async def delete_user(uuid: str, db: AsyncSession = Depends(get_session)):
    """Delete one user entry from database by uuid

    * `uuid`: User uuid
    """

    user = await user_crud.remove(db, uuid)
    if user is None:
        raise HTTPException(status_code=404, detail='Not found')
    return user
