from typing import List
from fastapi import APIRouter, Depends, Response, status

from models import MovieModel
from services import MovieService
from config import db

router = APIRouter(prefix="/movies", tags=["movies"])
service = MovieService(db)

@router.get("", response_description="List all students", response_model=List[MovieModel])
# async def get_movies_all(service: MovieService = db.get_db):
async def get_movies_all():
    

    print('route', service)
    return service.get_all()