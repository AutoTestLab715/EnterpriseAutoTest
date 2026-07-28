import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
ADMIN_URL = os.getenv("ADMIN_URL")

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

CONTENT_API = os.getenv("CONTENT_API")
LOGIN_API = os.getenv("LOGIN_API")


def require_config(name, value):
    if not value:
        raise RuntimeError(f"Missing config: {name}. Please check .env file.")
    return value