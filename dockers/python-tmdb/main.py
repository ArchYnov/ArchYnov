#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__copyright__ = "MIT"
__date__ = "2023-01-28"
__version__= "0.1.0"
__status__ = "Development"

"""
This project was developed to practice notions view in class mainly about database paradigms.
The contrains were to use different sources of data, in at least two different languages. 
We also had to use different databases with their own paradigms. 
Lastly we had to set up HDFS in any ways.

We decided to focuse on movies on this project, the reasons : a lot of free data online.
We choose to use 3 differents feeds:
TMDB -> The movie DataBase provide an API to fetch any data they had (https://www.themoviedb.org/).
Twitter -> The social media give access to every messages posted on their website (https://twitter.com/).
NewRSS -> Every now and then new articles are posted on their respective website waiting to be fetched (https://www.allocine.fr/) (https://screenrant.com/).

In term of database we use MongoDB (https://www.mongodb.com/), Elasticsearch (https://www.elastic.co/) and as we said before  HDFS (https://hadoop.apache.org/).
"""

from tools.redis import RedisClient
from tools.mongo import MongodbClient
from feeds.tmdbClient import TMDbClient
from fastapi import FastAPI
import uvicorn
from tools.redis import RedisClient

app = FastAPI()

client_redis = RedisClient()
client_redis.create_key_value("api_key_tmdb", '678b941591dc9bdb6ec1352563253fdd')
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
    # Fetch api key dans Redis
    try :
        tmdb_feed.fetchNewMovies()
        response = {
            "status": "success",
            "code": 200
        }
    except :
        response = {
            "status": "erreur dans l'insertion des données",
            "code": 500
        }

    return response