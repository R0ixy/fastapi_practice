import os

from dotenv import load_dotenv

load_dotenv()

DB_USER = os.environ.get('DB_user')
DB_PASSWORD = os.environ.get('DB_password')
DB_HOST = os.environ.get('DB_host')
SECRET_KEY = os.environ.get('SECRET_KEY')
