from sqlalchemy.orm import Session

from core.security import get_password_hash
from .. import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.CreateUser):
    password_hash = get_password_hash(user.password)
    db_user = models.User(
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
