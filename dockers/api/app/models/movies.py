from datetime import datetime
from pydantic import BaseModel, Field

from app.models.oid import PyObjectId

class MovieModel(BaseModel):
    oid: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    id: int | None = Field()
    adult: bool | None = Field()
    backdrop_path: str | None = Field()
    genre_ids: list[dict[str, str]] | None = Field()
    original_language: str | None = Field()
    original_title: str | None = Field()
    overview: str | None = Field()
    popularity: float | None = Field()
    poster_path: str | None = Field()
    release_date: datetime | None = Field()
    title: str | None = Field()
    video: bool | None = Field()
    vote_average: float | None = Field()
    vote_count: int | None = Field()
    encoded_pic: str | None = Field()

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            PyObjectId: str
        }


class MovieFilter(BaseModel):
    id: int | None
    adult: bool | None
    backdrop_path: str | None
    genre_ids: list | None
    original_language: str | None
    original_title: str | None
    overview: str | None
    popularity: float | None
    poster_path: str | None
    encoded_pic: str | None
    release_date: datetime | None
    title: str | None
    video: bool | None
    vote_average: float | None
    vote_count: int | None
