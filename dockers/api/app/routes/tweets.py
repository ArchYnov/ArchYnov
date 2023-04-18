from typing import Any
from fastapi import APIRouter, Depends, Request, Response, status
from pymongo import ASCENDING, DESCENDING

from app.models.tweets import TweetModel, TweetFilter
from app.services.tweets import TweetService
from app.utils.operator import check_operator, check_property, get_filter, get_value_type

router = APIRouter(prefix="/tweets", tags=["movies"])


def deps_service(request: Request):
    return TweetService(request.app.mongodb_client)


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
        if "id" not in fields:
            fields["id"] = 0
    # fields["_id"] = 0

    return {"filters": filters, "limit": limit, "offset": offset, "fields": fields, "sort": sort}


@router.options("/", status_code=status.HTTP_200_OK)
async def options():
    return {
        "methods": ["GET", "OPTIONS"],
    }

@router.get("/", response_description="Response all tweets", status_code=status.HTTP_200_OK)
async def all(service: TweetService = Depends(deps_service), params: dict = Depends(parameters)) -> Any:
    filters = params["filters"]
    limit = params["limit"]
    offset = params["offset"]
    fields = params["fields"]
    sort = params["sort"]

    query = {}
    projection = {}
    try:
        model_fields = TweetModel.__fields__
        properties = {field.name: field.alias for field in model_fields.values()}

        if fields:
            # projection = {properties[field]: fields[field] for field in fields if field in properties}
            for field in fields:
                keys = field.split(".")
                if keys[0] in properties:
                    c = f'{properties[keys[0]]}'
                    if len(keys) > 1:
                        for f in keys[1:]:
                            c += f'.{f}'
                    projection[c] = fields[field]

        if filters:
            # query = {properties[key]: { value["operator"]: value["value"] } for key, value in filters.items() if key in properties}
            for key, value in filters.items():
                keys = key.split(".")
                if keys[0] in properties:
                    c = f'{properties[keys[0]]}'
                    if len(keys) > 1:
                        for f in keys[1:]:
                            c += f'.{f}'
                    query[c] = { value["operator"]: value["value"] }
                    
    except Exception as e:
        print(e)
        return Response(status_code=status.HTTP_400_BAD_REQUEST, content=e.args[0])

    tweets = [TweetModel(**tweet).dict(exclude_unset=True) for tweet in service.find_by_filter(query, sort, limit, offset, projection)]
 
    if not tweets:
        return {
            "description": "Response all tweets",
            "count": 0,
            "result": []
        }

    return {
        "description": "Response all tweets",
        "count": len(tweets),
        "result": tweets
    }