from tweepy import OAuthHandler, API, Cursor
from tweepy.errors import TweepyException
from polyglot.detect import Detector

class TwitterClient(object):
    def __init__(self, db, client_redis, supported_languages=None):
        """ 
        DESC : initiate varibles and set-up the tweepy class for later usage

        IN   :  db - database where infos are going to be saved
                sentimentModule - sentiment analysis class analyse our string
                supported_language - only fetch certain languages (used for emoji conversion) (default is english) 
        """
        self.db = db
        if supported_languages and type(supported_languages) == list:
            self.supported_languages = supported_languages
        else:
            self.supported_languages = ['en']

        try:
            key = ["api_key","api_key_secret","access_token","access_token_secret"]
            tokens = client_redis.get_value_by_key(key)
            self.auth = OAuthHandler(tokens['api_key'], tokens['api_key_secret'])
            self.auth.set_access_token(tokens['access_token'], tokens['access_token_secret'])
            self.api = API(self.auth, wait_on_rate_limit=True)
            
        except:
            print('Error: Authentication Failed')

    def insertDb(self, tweets):
        """ 
        DESC : format tweet infos before sending them to the db

        IN   : array of dict containing every infos about their tweet 
        OUT  : array of sorted provided dict 
        """
        actions = []
        for tweet in tweets:
            actions.append({
                '_index': 'twitter',
                '_id': tweet.id_str,
                '_source': {
                    'date': tweet.created_at,
                    'text': tweet.full_text,
                    'nombre_retweet': tweet.retweet_count,
                    'nombre_like': tweet.favorite_count,
                },
                '_sentiment_analysis' : 'n/a'
            })
        self.db.insertMany("tweets", actions, ['_id'])
        
    def deleteDb(self):
        """ 
        DESC : ask the ElasticSearch db to delete every entries that came from twitter 
        """
        return self.db.deleteData('twitter')

    def getTweets(self, query, count=10):
        """ 
        DESC : download every tweets that match our query then keep only the ones that have the supported languages 

        IN   :  query - search input to fetch tweets
                count - number of tweet to download ( default is 10 )
        OUT  : array of dictionnary containing tweet infos
        """
        tweets = []
        try:
            for tweet in Cursor(self.api.search_tweets, q=query, tweet_mode='extended').items(count):
                language=Detector(tweet.full_text, quiet=True).language.code
                if language in self.supported_languages:
                    if tweet.retweet_count:
                        if tweet not in tweets:
                            tweets.append(tweet)
                    else:
                        tweets.append(tweet)
            return tweets
        except TweepyException as e:
            print('Error : ' + str(e))

    def pushNewTweets(self, query, count):
        """ 
        DESC : fetch tweets before sending formatted version of them to the DB

        IN   :  query - search input to fetch tweets
                count - number of tweet to download ( default is 10 )
        OUT  : result of the request
        """
        return self.insertDb(self.getTweets(query, count))

    def setSupportedLanguages(self, language):
        """ 
        DESC : basicd setter method

        IN   :  language - new supported language
        """
        self.supported_languages = language
