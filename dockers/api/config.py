from pydantic import BaseSettings

class Settings(BaseSettings):
    API_PREFIX: str = "/api/v1"
    MONGO_USERNAME: str = "root"
    MONGO_PASSWORD: str = "root"
    MONGO_DB_NAME: str = "ydays"
    MONGO_URL: str = "mongodb://root:root@mongo:27017/"
