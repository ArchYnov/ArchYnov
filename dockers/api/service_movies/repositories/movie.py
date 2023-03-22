
from config import Database
from models import MovieModel 
# from schemas import MovieSchema

class MovieRepository:
    def __init__(self, db):
        self._collection = db['tmdb']

    def get_all(self):
        movies = [MovieModel(**movie) for movie in self._collection.find()]
        return movies
        
    def get_by_id(self, id):
        movie = self._collection.find_one({'id': id})
        return MovieModel(**movie)
    
    def count(self):
        c = self._collection.count_documents({})
        print(c)
        return c

    # def create(self, movie: MovieSchema):
    #     new_movie = MovieModel(**movie.dict())
    #     self.db.add(new_movie)
    #     self.db.commit()
    #     self.db.refresh(new_movie)
    #     return new_movie

    # def update(self, id, movie: MovieSchema):
    #     movie = self.db.query(MovieModel).filter(MovieModel.id == id)
    #     movie.update(movie.dict())
    #     self.db.commit()
    #     return movie

    # def delete(self, id):
    #     movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
    #     self.db.delete(movie)
    #     self.db.commit()
    #     return movie
