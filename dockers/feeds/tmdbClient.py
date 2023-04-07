import tmdbsimple as tmdb
import requests
import os
import re
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

    def movieMenu(self):
        """
        DESC : Display a list of recent movies to choose from

        OUT  : the ID and title of the choosen movie
        """
        warning=''
        while True:
            # os.system(CLEAR_SYNTAXE)
            print('\n\nList of available movies :\n')
            for p, movie in enumerate(self.new_movies):
                print('{} : {}'.format(p, movie['original_title']))
            choice = input('\nWhat movie do you want info on ?\n{} > '.format(warning))
            # Test if choice is an Integer in the range of the menu
            if choice.isnumeric():
                choice=int(choice)
                if 0 <= choice <= p:
                    return self.new_movies[choice]['id'], re.sub(r'[^\w\-\. ]', '_', self.new_movies[choice]['original_title']), float(format(self.new_movies[choice]['vote_average']/2, '.1f'))
                else:
                    warning='An existing one this time...\n'
            else:
                warning='A number will work great too...\n'

    def downloadPic(self, movie_id):
        """
        DESC : Download a movie poster based on his ID

        IN   : movie_id - id of the movie that we'll download
        OUT  : file path
        """
        # Test if directory exists in working directory, if not, creates it
        if not os.path.isdir(self.img_dir_path):
            try:
                os.mkdir(self.img_dir_path)
                print('../images directory created')
            except Exception as e:
                print('Error :' + e +
                'Failed to create ../images directory, please launch in administrator privileges')
        
        url = 'https://www.themoviedb.org/t/p/w600_and_h900_bestv2/'+ \
                    tmdb.Movies(movie_id).info()['poster_path']
        img_path='{}/{}.{}'.format(self.img_dir_path, movie_id, url.split('.')[-1])
        # Test if file already exists if not, download it
        if not os.path.exists(img_path):
            response = requests.get(url, stream=True)
            if not response.ok:
                print('Failed to get image from Movie. Please try again ¯\_(ツ)_/¯')
                return 0
            with open(img_path, 'wb') as file:
                for block in response.iter_content(1024):
                    if not block: break
                    file.write(block)
            return img_path
        return img_path

    def deletePicDir(self):
        """
        DESC : Delete the directory used to store downloaded pictures

        OUT  : 0|1 success or not
        """
        if os.path.isdir(self.img_dir_path):
            for pic in os.listdir(self.img_dir_path):
                os.remove('{}/{}'.format(self.img_dir_path, pic))
            return os.rmdir(self.img_dir_path)
        else:
            return 0

    def fetchNewMovies(self):
        genre_transcript = {28: 'Action', 12: 'Adventure', 16: 'Animation', 35: 'Comedy', 80: 'Crime', 99: 'Documentary', 18: 'Drama', 10751: 'Family', 14: 'Fantasy', 36: 'History', 27: 'Horror', 10402: 'Music', 9648: 'Mystery', 10749: 'Romance', 878: 'Science Fiction', 10770: 'TV Movie', 53: 'Thriller',10752: 'War',37: 'Western',10759: 'Action & Adventure',10762: 'Kids',10763: 'News',10764: 'Reality',10765: 'Sci-Fi & Fantasy', 10766: 'Soap',10767: 'Talk',10768: 'War & Politics'}

        self.new_movies = [movie for movie in tmdb.Movies().now_playing()['results'] 
                        if AlphabetDetector().only_alphabet_chars(movie['original_title'], 'LATIN')]
        # Ajouter les genres sur les films Tmdb
        for index, movie in enumerate(self.new_movies):
            genres = movie['genre_ids']
            temp_genres = []
            for genre in genres:
                if genre in genre_transcript.keys():
                    temp_genres.append({ genre : genre_transcript[genre] })
            self.new_movies[index]['genre_ids'] = temp_genres

        return self.new_movies
    

        