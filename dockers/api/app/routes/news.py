from typing import Any
from fastapi import APIRouter, Depends, Request, Response, status
from pymongo import ASCENDING, DESCENDING

from app.models.news import NewsModel, NewsFilter
from app.services.news import NewsService
from app.utils.operator import check_operator, check_property, get_filter, get_value_type

router = APIRouter(prefix="/news", tags=["news"])

def deps_service(request: Request):
    return NewsService(request.app.mongodb_client)


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
    fields["_id"] = 0

    print(fields)
    print(sort)
    print(filters)

    return {"filters": filters, "limit": limit, "offset": offset, "fields": fields, "sort": sort}


@router.options("/", status_code=status.HTTP_200_OK)
async def options():
    return {
        "methods": ["GET", "OPTIONS"],
    }

@router.get("/", response_description="Response all news", status_code=status.HTTP_200_OK)
async def all(service: NewsService = Depends(deps_service), params: dict = Depends(parameters)) -> Any:
    filters = params["filters"]
    limit = params["limit"]
    offset = params["offset"]
    fields = params["fields"]
    sort = params["sort"]

    filters_dict = {}
    try:
        if filters:
            for key, value in filters.items():
                check_property(NewsFilter, key)
                check_operator(value["operator"])
                v = get_value_type(NewsFilter, key, value["value"])
                filters_dict[key] = { value["operator"]: v }

    except Exception as e:
        print(e)
        return Response(status_code=status.HTTP_400_BAD_REQUEST, content=e.args[0])
    
    news = [NewsModel(**new).dict(exclude_unset=True) for new in service.find_by_filter(filters_dict, sort, limit, offset, fields)]
    print(news[0])
 
    if not news:
        return {
            "description": "Response all news",
            "count": 0,
            "result": []
        }

    return {
        "description": "Response all news",
        "count": len(news),
        "result": news
    }