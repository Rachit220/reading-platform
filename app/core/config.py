import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite+aiosqlite:///./reading.db"
)

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "dev-secret-key-change-me"
)

ALGORITHM = "HS256"
