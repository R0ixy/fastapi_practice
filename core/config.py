import os

from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.environ.get('DB_name')
DB_PASSWORD = os.environ.get('DB_password')
