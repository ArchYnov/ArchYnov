from fastapi import FastAPI, Response
import json

from tools.redis_client import RedisClient
from tools.mongo import MongodbClient
from feeds.twitterClient import TwitterClient

app = FastAPI()

client_redis = RedisClient(host="redis")
client_mongo = MongodbClient()

twitter_feed = TwitterClient(client_mongo, client_redis, client_redis.get_value_by_key(["api_key","api_key_secret","access_token","access_token_secret"]))

@app.get("/fetchTwitter")
async def fetchTwitter():
    """ 
        DESC : Route to fetch tweets based on movie name and store data

        IN   : none
        OUT  : result of the request
    """
    # Fetch mongoDB movie list
    testCol = client_mongo.getAllDocumentsFromCollection("tmdb")
    all_movies = [ el["original_title"] for el in testCol ]
    for movie_name in all_movies:
        query = '#' + movie_name.replace(' ', '') + ' -filter:retweets'
        twitter_feed.pushNewTweets(query=query , count=10)
    return Response(
        status_code=200,
        content=json.dumps({"result": "sucess"}),
        media_type="application/json"
    )