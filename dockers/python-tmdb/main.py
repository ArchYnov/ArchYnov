from fastapi import FastAPI, Response
import json

from tools.redis_client import RedisClient
from tools.mongo import MongodbClient
from feeds.tmdbClient import TMDbClient

app = FastAPI()
client_redis = RedisClient(host="redis")
mongo_client= MongodbClient()
tmdb_feed = TMDbClient(
    mongo_client=mongo_client,
    api_key=client_redis.get_value_by_key(["api_key_tmdb"])['api_key_tmdb']
)

@app.get("/fetchTmdb")
async def fetchTmdb():
    """ 
        DESC : Route to fetch tmdb last movies 

        IN   : movie_name
        OUT  : result of the request
    """
    return Response(
        status_code=200,
        media_type="application/json",
        content=json.dumps({
            "result": tmdb_feed.fetchNewMovies()
        })
    )
    