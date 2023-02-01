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
from feeds.twitterClient import TwitterClient
from fastapi import FastAPI
from fastapi import Response
import json
import uvicorn

app = FastAPI()

TWITTER_MAX_FETCH = 3
# connect to redis
client_redis = RedisClient()
client_redis.create_key_value("api_key", 'MyjgoENpH5NcIaNklNzKrbcBD')
client_redis.create_key_value("api_key_secret", 'OFcquJlUYOYaOlwcNbSS59cDzI7ovxLZn92hGmivypL4FahtNk')
client_redis.create_key_value("access_token", '1377622154683019265-cbNJTqBWzPJ5CJDdUOVazLk518hOba')
client_redis.create_key_value("access_token_secret", 'Qjo3HWA2DPz7pF2RjVgobTGG6m8OKtZLmiYBYYIfCZHoY')
# client_redis.create_key_value("bearer_token", 'AAAAAAAAAAAAAAAAAAAAAPBNlgEAAAAAO1PAncTKlPq1BL2Zl%2FKMA7wJb%2Fk%3DhnyDOuxBoVSgZ6n3QIPPyEd0cnMSoVkt0tBXtxkrli5UJ7c5kz')

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
    testCol = client_mongo.getAllDocumentsFromCollection("testTwitter")
    all_movies = [ ele["title"] for ele in testCol ]
    print(all_movies)
    for movie_name in all_movies:
        twitter_feed.pushNewTweets(query=movie_name, count=TWITTER_MAX_FETCH)
    return Response(
            status_code=200,
            content=json.dumps({"result": "sucess"}),
            media_type="application/json"
        )