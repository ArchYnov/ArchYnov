#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__copyright__ = "MIT"
__date__ = "2023-01-28"
__version__= "0.1.0"
__status__ = "Development"

"""
This project was developed as a 'end of the year' project.

We decided to focuse on movies, the reasons : a lot of free data online.
We choose to use 3 differents feeds:
TMDB -> The movie DataBase provide an API to fetch any data they had (https://www.themoviedb.org/).
Twitter -> The social media give access to every messages posted on their website (https://twitter.com/).
NewRSS -> Every now and then new articles are posted on their respective website waiting to be fetched (https://www.allocine.fr/) (https://screenrant.com/).

In term of database we use MongoDB (https://www.mongodb.com/), as we said before  HDFS (https://hadoop.apache.org/) and Redis for API keys.
"""

from tools.mongo import MongodbClient
from feeds.rssClient import RSSClient
from fastapi import FastAPI
import uvicorn

app = FastAPI()

TWITTER_MAX_FETCH = 50

mongodb_client = MongodbClient()
rss_feed = RSSClient(db=mongodb_client, urls={
        "allocineaffiche": "https://www.allocine.fr/rss/news-cine.xml",
        "screenrant": "https://screenrant.com/feed/",
    })

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