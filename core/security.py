from datetime import datetime, timedelta

from jose import jwt, JWTError
from passlib.context import CryptContext

from core.config import settings

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def create_access_token(subject: str, expires_delta: timedelta | None = None):
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode = {"exp": expire, "uuid": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def generate_email_token(email: str):
    expire = datetime.utcnow() + timedelta(days=7)
    to_encode = {"exp": expire, "email": email}
    token = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return token


def verify_email_token(token: str):
    try:
        decode_token = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
        return decode_token
    except JWTError:
        return None
