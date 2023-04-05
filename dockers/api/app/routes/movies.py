from typing import List
from fastapi import APIRouter, Depends, Request, Response, status

from app.models.movies import MovieModel
from app.services.movies import MovieService

router = APIRouter(prefix="/movies", tags=["movies"])

def deps_service(request: Request):
    return MovieService(request.app.mongodb_client)

print(router.dependency_overrides_provider)
@router.get("/", response_description="Response all movies", status_code=status.HTTP_200_OK)
async def all(service: MovieService = Depends(deps_service), limit: int = 100, offset: int = 0):
    movies = [MovieModel(**movie) for movie in service.find(limit, offset)]
    
    if not movies:
        return {
            "description": "Response all movies",
            "count": 0,
            "result": []
        }

    return {
        "description": "Response all movies",
        "count": len(movies),
        "result": movies
    }

@router.get("/number", response_description="Reponse number movies", status_code=status.HTTP_200_OK)
async def number(service: MovieService = Depends(deps_service)):
    return {
        "description": "Reponse number movies",
        "result": service.count()
    }

@router.get("/{id}", response_description="Reponse movies by id", status_code=status.HTTP_200_OK)
async def by_id(response: Response, service: MovieService = Depends(deps_service), id: int | str = None):
    movie = service.find_by_id(id)

    if not movie:
        response.status_code = status.HTTP_404_NOT_FOUND  
        return {
            "description": "Reponse movies by id",
            "result": None
        }
    
    return {
        "description": "Reponse movies by id",
        "result": MovieModel(**movie)
    }
    