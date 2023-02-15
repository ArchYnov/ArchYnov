from sqlalchemy.orm import Session

from src.models import MovieModel 
from src.schemas.movie import MovieSchema

class MovieRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        movies = self.db.query(MovieModel).all()
        return movies

    def get_by_id(self, id):
        movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return movie

    def create(self, movie: MovieSchema):
        new_movie = MovieModel(**movie.dict())
        self.db.add(new_movie)
        self.db.commit()
        self.db.refresh(new_movie)
        return new_movie

    def update(self, id, movie: MovieSchema):
        movie = self.db.query(MovieModel).filter(MovieModel.id == id)
        movie.update(movie.dict())
        self.db.commit()
        return movie

    def delete(self, id):
        movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        self.db.delete(movie)
        self.db.commit()
        return movie
