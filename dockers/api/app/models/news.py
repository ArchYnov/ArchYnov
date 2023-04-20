from datetime import datetime
from pydantic import BaseModel, Field

from app.models.oid import PyObjectId

class SourceModel(BaseModel):
    title: str | None = Field()
    text: str | None = Field()
    date: datetime | None = Field()

class SetimentAnalysisModel(BaseModel):
    label: str | None = Field()
    score: float | None = Field()

class NewsModel(BaseModel):
    id: str = Field(default_factory=PyObjectId, alias="_id")
    index: str | None = Field(alias="_index")
    source: SourceModel | None = Field(alias="_source")
    sentiment_analysis: SetimentAnalysisModel | str | None = Field(alias="_sentiment_analysis")

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            PyObjectId: str
        }

class NewsFilter(BaseModel):
    index: str | None
    source: dict | None
    sentiment_analysis: dict | None
