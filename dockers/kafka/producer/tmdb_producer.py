from json import dumps, loads
from kafka import KafkaProducer
from time import sleep
import requests
from requests import ConnectionError

print(" - Application started!")
producer = KafkaProducer(bootstrap_servers="kafka:29092",value_serializer=lambda x: dumps(x).encode("utf-8"))
print("Producer initialized.")

url = 'http://python-tmdb:5001/fetchTmdb'
while True:
    try:
        print(f"Fetching -> {url}")
        contents = loads(requests.get(url).content)
        print(f"Fetch sucessfull ! Sending data to consumers...")
        for content in contents["result"]:
            producer.send("tmdb", content)
        print(f"All the data has beem sent.")
        wait_time = 60*60
    except ConnectionError as error:
        print("erreur lors de la récupération de l'api")
        print(error)
        wait_time = 60
    print("Wait...")
    sleep(wait_time)
