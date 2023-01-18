from pydantic import BaseModel
from typing import Optional

class MovieSchema(BaseModel):
    id: int 
    title: str | None = None
    year: int | None = None

    class Config:
        orm_mode = True

