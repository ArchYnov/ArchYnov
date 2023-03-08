import pathlib
from pydantic import BaseSettings

# Project Directories
ROOT = pathlib.Path(__file__).resolve().parent.parent
print(ROOT)

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    # MONGODB_URL: str = "mongodb://root:root@mongo:27017"
    # MONGODB_NAME: str = "ydays"
    # MONGODB_COLLECTION: str = "tmdb"
    MONGO_USERNAME: str
    MONGO_PASSWORD: str
    MONGO_DB_NAME: str
    MONGO_URL: str

    class Config:
        env_file = ROOT / ".env"
        env_file_encoding = "utf-8"


settings = Settings(_env_file=".env")

print(settings.Config.env_file)

print(settings)
