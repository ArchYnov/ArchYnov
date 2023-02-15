import pathlib
from pydantic import BaseSettings

# Project Directories
ROOT = pathlib.Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    MONGODB_URL = "mongodb://root:root@localhost:27017/?authSource=admin&readPreference=primary&ssl=false&directConnection=true"
    MONGODB_NAME = "mongodb"

    class Config:
        env_file = ROOT / ".env"

settings = Settings()