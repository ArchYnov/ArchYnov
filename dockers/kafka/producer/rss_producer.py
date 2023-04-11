from json import dumps, loads
from kafka import KafkaProducer
from time import sleep
import requests
from requests import ConnectionError

print(" - Application started!")
producer = KafkaProducer(bootstrap_servers="kafka:29092", value_serializer=lambda x: dumps(x).encode("utf-8"))
print("Producer initialized.")

url = "http://python-rss:5001/fetchRSS"
while True:
    try:
        print(f"Fetching -> {url}")
        contents = loads(requests.get(url).content)
        print(f"Fetch sucessfull ! Sending data to consumers...")
        for source, articles in contents:
            producer.send("rss", {"source": source, "articles": articles})
        print(f"All the data has beem sent.")
        wait_time = 60*60
    except ConnectionError as error:
        print("Fetch failed !")
        print(error)
        wait_time = 60
    print("Wait...")
    sleep(wait_time)
