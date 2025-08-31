from pydantic import BaseModel
from typing import Optional

class Genre(BaseModel):
    id_genre: Optional[int] = None
    genre_type: str
    abbreviation: str