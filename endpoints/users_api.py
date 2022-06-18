from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.user import UserCreate
from database import SessionLocal
from crud import get_users_from_db, create_user_db_entry

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/')
def get_users(db: Session = Depends(get_db)):
    return get_users_from_db(db)


# @router.get('/{id}')
# def get_one_user(id: int):
#     return {f'user:{id}'}


@router.post('/')
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user_db_entry(db, user)
    print(db_user)
