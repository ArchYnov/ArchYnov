from src.repositories import MovieRepository


class MovieService:
    def __init__(self, movie_repository: MovieRepository):
        self.movie_repository = movie_repository

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
