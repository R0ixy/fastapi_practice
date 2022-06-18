from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core.config import DB_NAME, DB_PASSWORD

SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_NAME}:{DB_PASSWORD}@localhost/fastapi_practice"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
