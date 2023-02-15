from config import Database
from repositories import MovieRepository


class MovieService:
    def __init__(self, db: Database):
        self.movie_repository = MovieRepository(db.get_db())

    def get_all(self):
        return self.movie_repository.get_all()

    def get_by_id(self, id):
        return self.movie_repository.get_by_id(id)

    def create(self, movie):
        return self.movie_repository.create(movie)

    def update(self, id, movie):
        return self.movie_repository.update(id, movie)

    def delete(self, id):
        return self.movie_repository.delete(id)
