from sqlalchemy import Column, Integer, String, Float
from ..config.database import Base

class MovieModel(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    year = Column(Integer)

    