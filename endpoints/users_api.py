from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud import user_crud
from schemas.user import UserCreate, User, UserLogIn
from database import SessionLocal

router = APIRouter()


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/')
async def get_all_users(db: Session = Depends(get_db)):
    return await user_crud.get_users(db)


@router.get('/{uuid}')
async def get_one_user(uuid: str, db: Session = Depends(get_db)):
    return await user_crud.get_by_uuid(db, uuid)


@router.post('')
@router.post('/')
async def create_user(user: UserCreate, db: Session = Depends(get_db)) -> User | None:
    db_user_by_email = await user_crud.get_by_email(db, user.email)
    if db_user_by_email:
        raise HTTPException(status_code=400, detail='Email is already registered')

    db_user_by_phone = await user_crud.get_by_phone(db, user.phoneNumber)
    if db_user_by_phone:
        raise HTTPException(status_code=400, detail='Phone number is already registered')

    return await user_crud.create_new(db, user)


@router.post('/login/')
async def login(user: UserLogIn, db: Session = Depends(get_db)):
    user = await user_crud.authenticate(db, user)
    if user is None:
        raise HTTPException(status_code=400, detail='Incorrect email or password')
    return user

# TODO make jwt authorization
