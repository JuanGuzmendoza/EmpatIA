from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class User(BaseModel):
    id_user: Optional[int] = None                  # AUTO_INCREMENT
    full_name: str                                 # NOT NULL
    username: Optional[str] = None                 # UNIQUE pero puede ser NULL
    email: EmailStr                                # NOT NULL + formato email
    password_user: str                             # NOT NULL
    national_id: str                               # NOT NULL
    age: int                                       # NOT NULL
    id_genre: int                                  # FK, NOT NULL
    country: str                                   # NOT NULL
    city: str                                      # NOT NULL
    phone: int                                     # NOT NULL
    emergency_contact: Optional[int] = None        # NULL permitido
    address: Optional[str] = None                  # NULL permitido
    user_profile: Optional[str] = None             # UNIQUE pero puede ser NULL
    created_at: Optional[datetime] = None          # generado en DB
    updated_at: Optional[datetime] = None          # generado/actualizado en DB
