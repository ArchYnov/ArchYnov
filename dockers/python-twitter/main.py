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

In term of database we use MongoDB (https://www.mongodb.com/), as we said before  HDFS (https://hadoop.apache.org/) and Redis for API keys.
"""

from tools.redis_client import RedisClient
from tools.mongo import MongodbClient
from feeds.twitterClient import TwitterClient
from fastapi import FastAPI, Response
import json

app = FastAPI()

TWITTER_MAX_FETCH = 890

client_redis = RedisClient(host="redis")
client_mongo = MongodbClient()

key = ["api_key","api_key_secret","access_token","access_token_secret"]
tokens = client_redis.get_value_by_key(key)

twitter_feed = TwitterClient(client_mongo, client_redis, tokens)

@app.get("/fetchTwitter")
async def fetchTwitter():
    """ 
        DESC : Route to fetch tweets based on movie name and store data

        IN   : none
        OUT  : result of the request
    """
    # Fetch mongoDB movie list
    testCol = client_mongo.getAllDocumentsFromCollection("tmdb")
    all_movies = [ ele["original_title"] for ele in testCol ]
    for movie_name in all_movies:
        query = '#' + movie_name.replace(' ', '') + ' -filter:retweets'
        twitter_feed.pushNewTweets(query=query , count=10)
    return Response(
            status_code=200,
            content=json.dumps({"result": "sucess"}),
            media_type="application/json"
        )