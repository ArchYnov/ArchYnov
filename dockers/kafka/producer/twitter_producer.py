from json import dumps, loads
from kafka import KafkaProducer
from time import sleep
from tools.mongo import MongodbClient
from tools.redis_client import RedisClient
from tools.mongo import MongodbClient
from feeds.twitterClient import TwitterClient

MONGODB_CLIENT = MongodbClient()

print(" Twitter - Application started!")
producer = KafkaProducer(bootstrap_servers="kafka:29092",value_serializer=lambda x: dumps(x).encode("utf-8"))
fetch_max = 950
client_redis = RedisClient(host="redis")
client_mongo = MongodbClient()
twitter_feed = TwitterClient(client_mongo, client_redis, client_redis.get_value_by_key(["api_key","api_key_secret","access_token","access_token_secret"]))

print("Producer initialized.")

while True:
    try:
        nb_doc = MONGODB_CLIENT.getCollection("tmdb").count_documents({})
        print("start")
        testCol = client_mongo.getAllDocumentsFromCollection("tmdb", column={"_id": 1, "original_title": 1})
        all_movies = [{"_id": ele["_id"], "original_title": ele["original_title"]} for ele in testCol]
        contents = []
        for movie_name in all_movies:
            query = '#' + movie_name["original_title"].replace(' ', '') + ' -filter:retweets'
            contents += twitter_feed.pushNewTweets(query=query , count=2, movie_id=movie_name["_id"])
        for content in contents:
            producer.send("twitter", content)
        print("Fetch")
        print(f'Waiting for : {3600/((950/nb_doc)/2)} secs')
    except :
        print("Erreur lors de la récupération de l'api")
    sleep(3600/((950/nb_doc)/2))