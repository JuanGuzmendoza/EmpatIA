from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# Schema base (atributos comunes)
class UserBase(BaseModel):
    full_name: str
    username: Optional[str] = None
    email: EmailStr
    national_id: str
    age: int
    id_genre: int
    country: str
    city: str
    phone: int
    emergency_contact: Optional[int] = None
    address: Optional[str] = None
    user_profile: Optional[str] = None


# Schema para creación (incluye contraseña)
class UserCreate(UserBase):
    password_user: str


# Schema de respuesta (lo que se retorna al cliente)
class UserResponse(UserBase):
    id_user: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # permite convertir desde modelos ORM
