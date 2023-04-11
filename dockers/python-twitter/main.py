from fastapi import FastAPI, Response
import json

from tools.redis_client import RedisClient
from tools.mongo import MongodbClient
from feeds.twitterClient import TwitterClient
from fastapi import FastAPI
from fastapi import Response
import json
import uvicorn
from datetime import datetime

app = FastAPI()

client_redis = RedisClient(host="redis")
client_mongo = MongodbClient()

twitter_feed = TwitterClient(client_mongo, client_redis, client_redis.get_value_by_key(["api_key","api_key_secret","access_token","access_token_secret"]))

def datetime_handler(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()

@app.get("/fetchTwitter")
async def fetchTwitter():
    """ 
        DESC : Route to fetch tweets based on movie name and store data

        IN   : none
        OUT  : result of the request
    """
    # Fetch mongoDB movie list

    testCol = client_mongo.getAllDocumentsFromCollection("tmdb", column={"_id": 1, "original_title": 1})
    all_movies = [{"_id": ele["_id"], "original_title": ele["original_title"]} for ele in testCol]
    tweets = []
    for movie_name in all_movies:
        query = '#' + movie_name["original_title"].replace(' ', '') + ' -filter:retweets'
        tweets += twitter_feed.pushNewTweets(query=query , count=2, movie_id=movie_name["_id"])
    return Response(
            status_code=200,
            content=json.dumps({"result": tweets}, default=datetime_handler),
            media_type="application/json"
        )
