import pathlib

from pydantic import BaseSettings

# Project Directories
ROOT = pathlib.Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    MONGO_USERNAME: str
    MONGO_PASSWORD: str
    MONGO_DB_NAME: str
    MONGO_URL: str

    class Config:
        env_file = ROOT / ".env"
        env_file_encoding = "utf-8"
