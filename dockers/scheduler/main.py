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

from datetime import datetime
import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger

scheduler = BlockingScheduler()
@scheduler.scheduled_job(IntervalTrigger(hours=3))
def launchFetches():
    if requests.get('0.0.0.0:5002/fetchTmdb') == 200 : "Tmbd Fetch OK"
    if requests.get('0.0.0.0:5002/fetchTwitter') == 200 : "Twitter Fetch OK"
    if requests.get('0.0.0.0:5002/fetchRss') == 200 : "RSS Fetch OK"

scheduler.start()