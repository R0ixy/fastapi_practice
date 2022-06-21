from pydantic import BaseModel, constr, UUID4, EmailStr


# from pydantic import constr, UUID4


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
    email: EmailStr
    password: str


class User(UserBase):
    """
    User class for database interaction
    """
    user_id: int
    user_uuid: UUID4
    hashed_password: str
    is_active: bool

    class Config:
        orm_mode = True
