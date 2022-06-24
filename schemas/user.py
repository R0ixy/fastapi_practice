from pydantic import BaseModel, constr, UUID4, EmailStr


class UserBase(BaseModel):
    """
    Base user class
    """
    firstName: str
    lastName: str
    email: EmailStr
    phoneNumber: constr(
        strip_whitespace=True,
        regex=r'^\+?3?8?(0[5-9][0-9]\d{7})$'
    )
    # TODO fix phone regex to work with all numbers (Now working only with Ukrainian)


class UserCreate(UserBase):
    """
    User class with all fields for new entry creation
    """
    password: str

    # class Config:
    #     orm_mode = True


class UserLogIn(BaseModel):
    """User class with all fields for login"""
    email: EmailStr
    password: str


class User(UserBase):
    """User class with all fields for response"""
    uuid: UUID4

    class Config:
        orm_mode = True


class UserInDB(UserBase):
    """User class with all fields for existing entry"""

    user_id: int
    uuid: UUID4
    hashed_password: str
    is_active: bool

    class Config:
        orm_mode = True
