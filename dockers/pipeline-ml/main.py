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

import schedule
import time
from tools.mongo import MongodbClient
from transformers import pipeline

client_mongo = MongodbClient()

def main():
    # set query to fetch the documents where Sentiment Analysis isn't defined
    query = { '_sentiment_analysis': 'n/a' }
    # send query
    print("Fetching datas...")
    tweets       = client_mongo.get_documents('tweets', query)
    rss_articles = client_mongo.get_documents('rss', query)

    print("Fetch done !")

    sentiment_pipeline = pipeline("sentiment-analysis")
    tweet_analysed = sentiment_pipeline([ele[1] for ele in tweets])
    rss_analysed = sentiment_pipeline([ele[1] for ele in rss_articles])

    for index, value in enumerate(tweets):
        client_mongo.update_one('tweets', { "_id" : value[0] }, { "$set" :{ "_sentiment_analysis" : tweet_analysed[index] } })
    for index, value in enumerate(rss_articles):
        client_mongo.update_one('rss', { "_id" : value[0] }, { "$set" :{ "_sentiment_analysis" : rss_analysed[index] } })

    print(f'Added sentiment analysis for {len(tweet_analysed)} tweets and {len(rss_analysed)} rss articles.')
    return

schedule.every(1).minutes.do(main)

if __name__ == '__main__':
    main()