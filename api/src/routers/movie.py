from fastapi import APIRouter, Depends, Response, status

from src.services import MovieService
from src.config import DatabaseNoSQL as Database

router = APIRouter(prefix="/movies", tags=["movies"])

@router.get("/")
async def get_movies_all(service: MovieService = Depends(Database.session())):
    return service.get_movies()