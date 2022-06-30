from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    SECRET_KEY: str

    CELERY_USER: str
    CELERY_PASSWORD: str
    CELERY_HOST: str

    SMTP_SERVER: str
    SMTP_PORT: int
    SMTP_LOGIN: str
    SMTP_PASSWORD: str

    class Config:
        env_file = '.env'


settings = Settings()
