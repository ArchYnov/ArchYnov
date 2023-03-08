from typing import List
from fastapi import APIRouter, Depends, Response, status

from models import MovieModel
from services import MovieService
from config import db

router = APIRouter(prefix="/movies", tags=["movies"])
service = MovieService(db)

@router.get("", response_description="Response all movies", response_model=List[MovieModel])
# async def get_movies_all(service: MovieService = db.get_db):
async def movies_all():
    return service.get_all()

@router.get("/{id}", response_description="Reponse movies by id", response_model=MovieModel)
async def movies_by_id(id: int):
    return service.get_by_id(id)