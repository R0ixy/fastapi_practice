from sqlalchemy.orm import Session

from core.security import get_password_hash, verify_password
from models import User
from schemas import UserCreate
from crud.base_crud import CRUDbase


class UserCRUD(CRUDbase):

    async def get_by_email(self, db: Session, email: str):
        return db.query(self.model).filter_by(email=email).first()

    async def get_by_phone(self, db: Session, phone: str):
        return db.query(self.model).filter_by(phoneNumber=phone).first()

    async def create_new(self, db: Session, obj: UserCreate):
        db_user = self.model(
            firstName=obj.firstName,
            lastName=obj.lastName,
            phoneNumber=obj.phoneNumber,
            email=obj.email,
            hashed_password=get_password_hash(obj.password)
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    async def authenticate(self, db: Session, obj):
        user = await self.get_by_email(db, obj.email)
        if user is None:
            return None
        if not verify_password(obj.password, user.hashed_password):
            return None
        return user


user_crud = UserCRUD(User)
