import tmdbsimple as tmdb
import requests
import os
import base64
from alphabet_detector import AlphabetDetector
from sys import platform


CLEAR_SYNTAXE = 'cls' if platform == 'win32' else 'clear'


class TMDbClient(object):
    def __init__(self, mongo_client, api_key, img_dir_path=os.path.join(os.getcwd(), 'images')):
        """
        DESC : set up tmdb API and fetch actu

        IN   : img_dir_path -  define the image dir ( default is eq to <mainApp>/images ) 
        """
        tmdb.API_KEY = api_key
        tmdb.REQUESTS_TIMEOUT = 10
        tmdb.REQUESTS_SESSION = requests.Session()
        
        self.img_dir_path = img_dir_path
        self.mongo_client = mongo_client

    def downloadPic(self, poster_path):
        """
        DESC : Download a movie poster based on his ID

        IN   : poster_path
        OUT  : file path
        """
        return base64.b64encode(requests.get(
            f'https://www.themoviedb.org/t/p/w600_and_h900_bestv2{poster_path}'
        ).content)

    def fetchNewMovies(self):
        for movie in tmdb.Movies().now_playing()['results']:
            if AlphabetDetector().only_alphabet_chars(movie['original_title'], 'LATIN'):
                movie["encoded_pic"] = self.downloadPic(movie['poster_path'])
                self.new_movies.append(movie)
        # Ajouter propriété nbFetchTwitter et nbFetchRss
        return self.new_movies
    

        