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
        OUT  : base64 encoded poster
        """
        return base64.b64encode(requests.get(
            f'https://www.themoviedb.org/t/p/w600_and_h900_bestv2{poster_path}'
        ).content)

    def fetchNewMovies(self):
        try :
            genre_transcript = {
                28: 'Action',
                12: 'Adventure',
                16: 'Animation',
                35: 'Comedy',
                0: 'Crime',
                99: 'Documentary',
                18: 'Drama',
                10751: 'Family',
                14: 'Fantasy',
                36: 'History',
                27: 'Horror',
                10402: 'Music',
                9648: 'Mystery',
                10749: 'Romance',
                878: 'Science Fiction',
                10770: 'TV Movie',
                53: 'Thriller',
                10752: 'War',
                37: 'Western',
                10759: 'Action & Adventure',
                10762: 'Kids',
                10763: 'News',
                10764: 'Reality',
                10765: 'Sci-Fi & Fantasy',
                10766: 'Soap',
                10767: 'Talk',
                10768: 'War & Politics'
            }
            self.new_movies = []
            for movie in tmdb.Movies().now_playing()['results']:
                if AlphabetDetector().only_alphabet_chars(movie['original_title'], 'LATIN'):
                    movie["encoded_pic"] = self.downloadPic(movie['poster_path'])
                    self.new_movies.append(movie)

            # Ajouter les genres sur les films Tmdb
            for index, movie in enumerate(self.new_movies):
                temp_genres = []
                for genre in movie['genre_ids']:
                    if genre in genre_transcript.keys():
                        temp_genres.append({ genre : genre_transcript[genre] })
                self.new_movies[index]['genre_ids'] = temp_genres
            return self.new_movies
        except Exception as e :
            return e
