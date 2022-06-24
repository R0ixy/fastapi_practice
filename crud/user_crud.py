from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from core.security import get_password_hash, verify_password
from models import User
from schemas import UserCreate
from crud.base_crud import CRUDbase


class UserCRUD(CRUDbase):

    async def get_by_email(self, db: AsyncSession, email: str):
        """Get one user entry from database by email
        * `email`: User email"""
        query = select(self._model.email).where(self._model.email == email)
        users = await db.execute(query)
        user = users.first()
        return user

    async def get_by_phone(self, db: AsyncSession, phone: str):
        """Get one user entry from database by phone
        * `phone`: User phone"""
        query = select(self._model.phoneNumber).where(self._model.phoneNumber == phone)
        users = await db.execute(query)
        user = users.first()
        return user

    async def create_new(self, db: AsyncSession, obj: UserCreate):
        """Create new user in database
        * `obj`: User object"""
        db_user = self._model(
            firstName=obj.firstName,
            lastName=obj.lastName,
            phoneNumber=obj.phoneNumber,
            email=obj.email,
            hashed_password=get_password_hash(obj.password)
        )
        db.add(db_user)

        try:
            await db.commit()
            await db.refresh(db_user)
        except Exception:
            await db.rollback()
            raise
        return db_user

    async def authenticate(self, db: AsyncSession, obj):
        user = await self.get_by_email(db, obj.email)
        if user is None:
            return None
        if not verify_password(obj.password, user.hashed_password):
            return None
        return user


user_crud = UserCRUD(User)
