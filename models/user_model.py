from uuid import uuid4

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.dialects.postgresql import UUID

from database import Base


class User(Base):
    __tablename__ = "users"
    uuid = Column(UUID(as_uuid=True), primary_key=True, nullable=False, index=True, default=uuid4)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    phoneNumber = Column(String(14), unique=True, nullable=False, index=True)
    hashed_password = Column(String(60), nullable=False)
    is_active = Column(Boolean, default=0)
    is_superuser = Column(Boolean, default=0)
