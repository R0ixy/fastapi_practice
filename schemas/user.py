from pydantic import BaseModel
from pydantic import constr, UUID4


class UserBase(BaseModel):
    """
    Base user class
    """
    firstName: str
    lastName: str
    email: constr(
        regex=r'^[\w.+\-]+@gmail\.com$'
    )
    phoneNumber: constr(
        strip_whitespace=True,
        regex=r'^\+?3?8?(0[5-9][0-9]\d{7})$'
    )
    # TODO fix phone regex to work with all numbers (Now working only with Ukrainian)
    # TODO fix email regex to work all email domains (Now working only with gmail)


class UserCreate(UserBase):
    """
    User class with all fields for new entry creation
    """
    password: str

    # class Config:
    #     orm_mode = True


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
