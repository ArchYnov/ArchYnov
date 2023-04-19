from typing import Any
from fastapi import APIRouter, Depends, Request, Response, status
from pymongo import ASCENDING, DESCENDING

from app.models.movies import MovieModel, MovieFilter
from app.services.movies import MovieService
from app.utils.operator import check_operator, check_property, get_filter, get_value_type

router = APIRouter(prefix="/movies", tags=["movies"])


def deps_service(request: Request):
    return MovieService(request.app.mongodb_client)


def parameters(filters: str = None, limit: int = 100, offset: int = 0, fields: str = {}, sort: str = None):
    if sort:
        sort = sort.split(",")
        sort = [(field[1:], DESCENDING) if field[0] == "-" else (field, ASCENDING) for field in sort]
    else:
        sort = [("id", ASCENDING)]

    if filters:
        filters = filters.split(";")
        filters = get_filter(filters)

    if fields:
        fields = fields.split(",")
        fields = {field: 1 for field in fields}
    # fields["_id"] = 1

    return {"filters": filters, "limit": limit, "offset": offset, "fields": fields, "sort": sort}


@router.options("/", status_code=status.HTTP_200_OK)
async def options():
    return {
        "methods": ["GET", "OPTIONS"],
    }

@router.get("/", response_description="Response all movies", status_code=status.HTTP_200_OK)
async def all(service: MovieService = Depends(deps_service), params: dict = Depends(parameters)):
    filters = params["filters"]
    limit = params["limit"]
    offset = params["offset"]
    fields = params["fields"]
    sort = params["sort"]

    filters_dict = {}
    try:
        if filters:
            for key, value in filters.items():
                check_property(MovieFilter, key)
                check_operator(value["operator"])
                v = get_value_type(MovieFilter, key, value["value"])

                if key == "genre_ids":
                    if value["operator"] == "$in" or value["operator"] == "$nin":
                        filters_dict[f'{key}.title'] = {value["operator"]: v}
                    else:
                        filters_dict[f'{key}.title'] = {"$all": v}
                else:
                    filters_dict[key] = { value["operator"]: v }
    except Exception as e:
        print(e)
        return Response(status_code=status.HTTP_400_BAD_REQUEST, content=e.args[0])
    
    # dd = service.find_by_filter(filters_dict, sort, limit, offset, fields)
    # print(MovieModel(**dd[0]))
    
    movies = [MovieModel(**movie) for movie in service.find_by_filter(filters_dict, sort, limit, offset, fields)]
 
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


@router.get("/best", response_description="Response best movies", status_code=status.HTTP_200_OK)
async def best(service: MovieService = Depends(deps_service), limit: int = 100, offset: int = 0):
    filters_dict = {}
    sort_dict = [("popularity", DESCENDING)]
    movies = [MovieModel(
        **movie) for movie in service.find_by_filter(filters_dict, sort_dict, limit, offset)]

    if not movies:
        return {
            "description": "Response best movies",
            "count": 0,
            "result": []
        }

    return {
        "description": "Response best movies",
        "count": len(movies),
        "result": movies
    }


@router.get("/new", response_description="Response new movies", status_code=status.HTTP_200_OK)
async def new(service: MovieService = Depends(deps_service), limit: int = 100, offset: int = 0):
    filters_dict = {}
    sort_dict = [("release_date", DESCENDING)]
    movies = [MovieModel(
        **movie) for movie in service.find_by_filter(filters_dict, sort_dict, limit, offset)]

    if not movies:
        return {
            "description": "Response new movies",
            "count": 0,
            "result": []
        }

    return {
        "description": "Response new movies",
        "count": len(movies),
        "result": movies
    }


@router.get("/number", response_description="Reponse number movies", status_code=status.HTTP_200_OK)
async def number(service: MovieService = Depends(deps_service)):

    return {
        "description": "Reponse number movies",
        "result": service.count()
    }

@router.get("/genres", response_description="Reponse all genres", status_code=status.HTTP_200_OK)
async def genres(service: MovieService = Depends(deps_service)):
    genres = service.distinct("genre_ids.title", {})

    if not genres:
        return {
            "description": "Reponse all genres",
            "count": 0,
            "result": []
        }

    return {
        "description": "Reponse all genres",
        "count": len(genres),
        "result": genres
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
