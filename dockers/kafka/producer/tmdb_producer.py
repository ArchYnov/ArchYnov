from json import dumps, loads
from kafka import KafkaProducer
from time import sleep
import requests

producer = KafkaProducer(bootstrap_servers="kafka:29092",value_serializer=lambda x: dumps(x).encode("utf-8"))

while True:
    try:
        # on recupere le content de la route fetchTmdb que l'on convertit de bytes -> list(dict)
        contents = requests.get('http://python-tmdb:5002/fetchTmdb').content
        contents = loads(contents.decode("utf-8"))
        for content in contents["result"]:
            producer.send("tmdb", content)
    except:
        print("erreur lors de la récupération de l'api")
    # A MODIFIER, on veut pas recuperer les films toutes les 5 secondes
    sleep(5)
