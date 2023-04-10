#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__copyright__ = "MIT"
__date__ = "2023-01-28"
__version__= "0.1.0"
__status__ = "Development"

"""
This project was developed as a 'end of the year' project.

We decided to focuse on movies, the reasons : a lot of free data online.
We choose to use 3 differents feeds:
TMDB -> The movie DataBase provide an API to fetch any data they had (https://www.themoviedb.org/).
Twitter -> The social media give access to every messages posted on their website (https://twitter.com/).
NewRSS -> Every now and then new articles are posted on their respective website waiting to be fetched (https://www.allocine.fr/) (https://screenrant.com/).

In term of database we use MongoDB (https://www.mongodb.com/), Elasticsearch (https://www.elastic.co/).
"""

from tools.redis_client import RedisClient
from tools.mongo import MongodbClient
from feeds.tmdbClient import TMDbClient
from fastapi import FastAPI, Response
import json

app = FastAPI()
client_redis = RedisClient(host="redis")

api_key = client_redis.get_value_by_key(["api_key_tmdb"])
mongodb_client = MongodbClient()
tmdb_feed = TMDbClient(mongo_client=mongodb_client, api_key=api_key['api_key_tmdb'])

@app.get("/fetchTmdb")
async def fetchTmdb():
    """ 
        DESC : Route to fetch tmdb based on movie name and store data

        IN   : movie_name
        OUT  : result of the request
    """
    return Response(
    status_code=200,
    content=json.dumps({"result": tmdb_feed.fetchNewMovies()}),
    media_type="application/json"
    )
    