from pydantic import BaseModel
from typing import Optional

class MovieSchema(BaseModel):
    id: str
    adult: bool = None
    backdrop_path: str = None
    belongs_to_collection: object = None
    budget: int = None
    genres: list = None

    class Config:
        arbitrary_types_allowed = True
