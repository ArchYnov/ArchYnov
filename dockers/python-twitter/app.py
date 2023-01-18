import pickledb
from tools.elasticSearch import ElasticSearchClient
from tools.sentimentAnalysis import SentimentAnalysis
from feeds.twitterClient import TwitterClient
from fastapi import FastAPI

app = FastAPI()

db_pickle = pickledb.load('project.db', False) 
db_pickle.set('api_key', 'lQQaJPtSdyKab6zyi03lHSanu') 
db_pickle.set('api_key_secret', 'texLfA0KI0VW428WMiPW5motO0z8PURFKvrJz0amktmGd0c3yK') 
db_pickle.set('access_token', '1377622154683019265-RnmvsG8dt06VAdOvlcHhEaYZs6lVD0') 
db_pickle.set('access_token_secret', 'SvWonpPDxsE3hNUfj2lrPjEvGb2Xj61tiJMWon0EKdEeg')
elasticSearchClient = ElasticSearchClient()
sentimentAnalysis = SentimentAnalysis()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/fetchTwitter/{movie_name}")
async def fetchTwitter(movie_name):
    twitter_feed = TwitterClient(elasticSearchClient, db_pickle, sentimentAnalysis)
    
    twitter_feed.pushNewTweets(query=movie['original_title'], count=TWITTER_MAX_FETCH)
    return {"message": "Hello World"}