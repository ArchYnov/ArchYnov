from json import dumps, loads
from kafka import KafkaProducer
from time import sleep
import requests
from requests import ConnectionError
from tools.redis_client import RedisClient
from tools.mongo import MongodbClient
from feeds.tmdbClient import TMDbClient

print(" TMDB - Application started!")
producer = KafkaProducer(bootstrap_servers="kafka:29092",value_serializer=lambda x: dumps(x).encode("utf-8"))
client_redis = RedisClient(host="redis")
mongo_client= MongodbClient()
tmdb_feed = TMDbClient(
    mongo_client=mongo_client,
    api_key=client_redis.get_value_by_key(["api_key_tmdb"])['api_key_tmdb']
)
print("Producer initialized.")

while True:
    try:
        print(f"Fetching ...")
        contents = tmdb_feed.fetchNewMovies()
        print(f"Fetch sucessfull ! Sending data to consumers...")
        for content in contents:
            producer.send("tmdb", content)
        print(f"All the data has beem sent.")
        wait_time = 60*60
    except ConnectionError as error:
        print("erreur lors de la récupération de l'api")
        print(error)
        wait_time = 60
    print("Wait...")
    sleep(wait_time)
