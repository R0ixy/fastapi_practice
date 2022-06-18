from uuid import uuid4

from sqlalchemy import Column, Integer, String, Boolean

from database import Base


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    user_uuid = Column(String(36), unique=True, nullable=False, default=uuid4)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    phoneNumber = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=0)
