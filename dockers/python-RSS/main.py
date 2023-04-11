from fastapi import FastAPI

from tools.mongo import MongodbClient
from feeds.rssClient import RSSClient

app = FastAPI()

mongodb_client = MongodbClient()
rss_feed = RSSClient(
    db=mongodb_client,
    urls={
        "allocineaffiche": "https://www.allocine.fr/rss/news-cine.xml",
        "screenrant": "https://screenrant.com/feed/",
    }
)

@app.get("/fetchRSS")
async def fetchRSS():
    """ 
        DESC : Route to fetch RSS flux based on provided URLs and store data

        IN   : None
        OUT  : result of the request
    """
    # for source, articles in self.getArticlesFromRSS():
    #             self.insertDb(source, articles)
    return rss_feed.pushNewArticles()