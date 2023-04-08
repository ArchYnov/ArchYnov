from fastapi import APIRouter, Depends, Request, Response, status
from pymongo import ASCENDING, DESCENDING

from app.models.movies import MovieModel, MovieFilter
from app.services.movies import MovieService
from app.utils.operator import check_operator, check_property, get_filter, get_value_type

router = APIRouter(prefix="/movies", tags=["movies"])

def deps_service(request: Request):
    return MovieService(request.app.mongodb_client)

def parameters(filters: str = None, limit: int = 100, offset: int = 0):
    # print(filters)
    if filters:
        filters = filters.split(";")
        filters = get_filter(filters)
        # print(filters)
    return {"filters": filters, "limit": limit, "offset": offset}



@router.options("/", status_code=status.HTTP_200_OK)
async def options():
    return {
        "methods": ["GET", "OPTIONS"],
    }

# print(router.dependency_overrides_provider)
# async def all(service: MovieService = Depends(deps_service), limit: int = 100, offset: int = 0, filters: str = None):
@router.get("/", response_description="Response all movies", status_code=status.HTTP_200_OK)
async def all(service: MovieService = Depends(deps_service), params: dict = Depends(parameters)):
    # print(params)
    filters = params["filters"]
    limit = params["limit"]
    offset = params["offset"]

    filters_dict = {}
    sort_dict = [("id", ASCENDING)]
    genre_transcript = {28: 'Action', 12: 'Adventure', 16: 'Animation', 35: 'Comedy', 80: 'Crime', 99: 'Documentary', 18: 'Drama', 10751: 'Family', 14: 'Fantasy', 36: 'History', 27: 'Horror', 10402: 'Music', 9648: 'Mystery', 10749: 'Romance', 878: 'Science Fiction', 10770: 'TV Movie', 53: 'Thriller',10752: 'War',37: 'Western',10759: 'Action & Adventure',10762: 'Kids',10763: 'News',10764: 'Reality',10765: 'Sci-Fi & Fantasy', 10766: 'Soap',10767: 'Talk',10768: 'War & Politics'}
    try:
        if filters:
            for key, value in filters.items():
                check_property(MovieFilter, key)
                check_operator(value["operator"])
                v = get_value_type(MovieFilter, key, value["value"])

                if key == "genre_ids":
                    genre = [{str(g): genre_transcript[g]} for g in genre_transcript if genre_transcript[g] in v]
                    if not genre:
                        raise Exception("Genre not found")
                    if value["operator"] == "$in" or value["operator"] == "$nin":
                        # filters_dict[key] = {"$elemMatch": { value["operator"]: genre }}
                        filters_dict[key] = { value["operator"]: genre }
                    else:
                        filters_dict[key] = {"$all": genre }
                else:
                    filters_dict[key] = { value["operator"]: v }
            print(filters_dict)
    except Exception as e:
        print(e)
        return Response(status_code=status.HTTP_400_BAD_REQUEST, content=e.args[0])
    
    movies = [MovieModel(**movie) for movie in service.find_by_filter(filters_dict, sort_dict, limit, offset)]
    
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
    movies = [MovieModel(**movie) for movie in service.find_by_filter(filters_dict, sort_dict, limit, offset)]

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
    movies = [MovieModel(**movie) for movie in service.find_by_filter(filters_dict, sort_dict, limit, offset)]

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

    d = service.count_by_filter({})

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
    