from datetime import datetime
from pydantic import BaseModel, Field

from app.models.oid import PyObjectId

class SourceModel(BaseModel):
    title: str | None = Field()
    text: str | None = Field()
    date: datetime | None = Field()
    nombre_retweet: int | None = Field()
    nombre_like: int | None = Field()

class SetimentAnalysisModel(BaseModel):
    label: str | None = Field()
    score: float | None = Field()

class TweetModel(BaseModel):
    id: str = Field(default_factory=PyObjectId, alias="_id")
    index: str | None = Field(alias="_index")
    source: SourceModel | None = Field(alias="_source")
    tmdb_id: str | None = Field(alias="_tmdb_id")
    sentiment_analysis: SetimentAnalysisModel | str | None = Field(alias="_sentiment_analysis")
    query: str | None = Field(alias="_query")

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            PyObjectId: str
        }

class TweetFilter(BaseModel):
    index: str | None
    source: dict | None
    tmdb_id: dict | None
    sentiment_analysis: dict | None
    query: dict | None