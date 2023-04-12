from json import dumps, loads
from kafka import KafkaProducer
from time import sleep
import requests
from tools.mongo import MongodbClient
MONGODB_CLIENT = MongodbClient()

producer = KafkaProducer(bootstrap_servers="kafka:29092",value_serializer=lambda x: dumps(x).encode("utf-8"))
fetch_max = 950

while True:
    try:
        nb_doc = MONGODB_CLIENT.getCollection("tmdb").count_documents({})
        print("start")
        # on recupere le content de la route fetchTmdb que l'on convertit de bytes -> list(dict)
        contents = requests.get('http://python-twitter:5001/fetchTwitter').content
        contents = loads(contents.decode("utf-8"))
        for content in contents["result"]:
            producer.send("twitter", content)
        print("fetch")
        print(3600/((950/nb_doc)/2))
    except:
        print("erreur lors de la récupération de l'api")
    # A MODIFIER, on veut pas recuperer les films toutes les 5 secondes
    sleep(3600/((950/nb_doc)/2))