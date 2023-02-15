from fastapi import FastAPI

from config import settings
from config import db
from routes import movies_router

app = FastAPI(title="API")

app.include_router(movies_router, prefix=settings.API_V1_STR, tags=["api_v1"])