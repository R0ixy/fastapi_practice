from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
from schemas.user import UserCreate
from database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/')
def get_all_users(db: Session = Depends(get_db)):
    return crud.get_users_from_db(db)


@router.get('/{uuid}')
def get_one_user(uuid: str, db: Session = Depends(get_db)):
    return crud.get_user_by_uuid(db, uuid)


@router.post('/')
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user_by_email = crud.get_user_by_email(db, user.email)
    if db_user_by_email:
        raise HTTPException(status_code=400, detail="Email is already registered")

    db_user_by_phone = crud.get_user_by_phone(db, user.phoneNumber)
    if db_user_by_phone:
        raise HTTPException(status_code=400, detail="Phone number is already registered")

    return crud.create_user_db_entry(db, user)
