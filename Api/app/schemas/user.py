from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[int] = None
    name: str
    identification: str
    full_name: str
    age: int
    address: Optional[str] = None
    gender: Optional[str] = None
    psychological_history: Optional[str] = None
    risk_status: Optional[str] = None
