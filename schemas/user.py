from pydantic import BaseModel


class User(BaseModel):
    user_id: str
    firstName: str
    lastName: str
    email: str
    phoneNumber: int
    hashed_password: str
    is_active: bool = 0

    class Config:
        orm_mode = True


class CreateUser(User):
    password: str

# TODO additional inheritance for is_active field
