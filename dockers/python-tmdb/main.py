#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__copyright__ = "MIT"
__date__ = "2023-01-28"
__version__= "0.1.0"
__status__ = "Development"

"""
This project was developed to practice notions view in class mainly about database paradigms.
The contrains were to use different sources of data, in at least two different languages. 
We also had to use different databases with their own paradigms. 
Lastly we had to set up HDFS in any ways.

We decided to focuse on movies on this project, the reasons : a lot of free data online.
We choose to use 3 differents feeds:
TMDB -> The movie DataBase provide an API to fetch any data they had (https://www.themoviedb.org/).
Twitter -> The social media give access to every messages posted on their website (https://twitter.com/).
NewRSS -> Every now and then new articles are posted on their respective website waiting to be fetched (https://www.allocine.fr/) (https://screenrant.com/).

In term of database we use MongoDB (https://www.mongodb.com/), Elasticsearch (https://www.elastic.co/) and as we said before  HDFS (https://hadoop.apache.org/).
"""

from tools.redis import RedisClient
from tools.mongodb import MongodbClient
from feeds.tmdbClient import TMDbClient
from fastapi import FastAPI

app = FastAPI()

TWITTER_MAX_FETCH = 50
# db_pickle.set('api_key', 'lQQaJPtSdyKab6zyi03lHSanu') 
# db_pickle.set('api_key_secret', 'texLfA0KI0VW428WMiPW5motO0z8PURFKvrJz0amktmGd0c3yK') 
# db_pickle.set('access_token', '1377622154683019265-RnmvsG8dt06VAdOvlcHhEaYZs6lVD0') 
# db_pickle.set('access_token_secret', 'SvWonpPDxsE3hNUfj2lrPjEvGb2Xj61tiJMWon0EKdEeg')
mongodb_client = MongodbClient()
tmdb_feed = TMDbClient(mongodb_client)

@app.get("/fetchTmdb")
async def fetchTmdb():
    """ 
        DESC : Route to fetch tmdb based on movie name and store data

        IN   : movie_name
        OUT  : result of the request
    """
    # Fetch api key dans Redis
    tmdb_feed.fetchNewMovies()
    # Push data to DB
    return 200