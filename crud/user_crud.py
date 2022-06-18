from sqlalchemy.orm import Session

from core.security import get_password_hash
# import models, schemas
from models import User
from schemas import UserCreate


def get_users_from_db(db: Session):
    return db.query(User).all()


#
# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()
#
#
def get_user_by_uuid(db: Session, user_uuid: str):
    return db.query(User).filter(User.user_uuid == user_uuid).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_user_by_phone(db: Session, phone: str):
    return db.query(User).filter(User.phoneNumber == phone).first()


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(User).offset(skip).limit(limit).all()


def create_user_db_entry(db: Session, user: UserCreate):
    password_hash = get_password_hash(user.password)
    db_user = User(
        firstName=user.firstName,
        lastName=user.lastName,
        phoneNumber=user.phoneNumber,
        email=user.email,
        hashed_password=password_hash
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
