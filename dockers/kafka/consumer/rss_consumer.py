from json import loads
from kafka import KafkaConsumer
from tools.mongo import MongodbClient
from feeds.rssClient import RSSClient

print(" - Application started!")

MONGODB_CLIENT = MongodbClient()
RSS_CLIENT = RSSClient(db=MONGODB_CLIENT, urls={
        "allocineaffiche": "https://www.allocine.fr/rss/news-cine.xml",
        "screenrant": "https://screenrant.com/feed/",
    })
CHECK_DUPLICATES = ['_id']

# Create Kafka consumer
consumer = KafkaConsumer(
    "rss",
    bootstrap_servers=["kafka:29092"],
    api_version=(0, 10, 1),
)

for value in consumer:
    # on convertit les datas envoyer par le consumer bytes -> dict
    data = loads(value.value.decode("utf-8"))
    # try:
        # MONGODB_CLIENT.insertOne("tmdb", data, CHECK_DUPLICATES)
    RSS_CLIENT.insertDb(data["source"], data["articles"], CHECK_DUPLICATES)
    # except:
    #     print("erreur lors de l'insertion en base")