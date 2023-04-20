from json import loads
from kafka import KafkaConsumer
from tools.mongo import MongodbClient
from datetime import datetime
MONGODB_CLIENT = MongodbClient()

# Create Kafka consumer
consumer = KafkaConsumer(
    "twitter",
    bootstrap_servers=["kafka:29092"],
    api_version=(0, 10, 1),
)

for value in consumer:
    # on convertit les datas envoyer par le consumer bytes -> dict
    data = loads(value.value.decode("utf-8"))
    print(data)
    try:
        data["_source"]["date"] = datetime.strptime(data["_source"]["date"], "%Y-%m-%dT%H:%M:%S%z")
        MONGODB_CLIENT.insertOne("tweets", data, ['_id'])
        print("Insertion en base réussis")
    except :
        print("Erreur lors de l'insertion en base")