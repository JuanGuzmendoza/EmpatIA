from pydantic import BaseModel

class UserSchema(BaseModel):
    id_user: int
    nombre: str | None = None
    telefono: str | None = None
    edad: str | None = None
    historial_clinico: str | None = None

    class Config:
        orm_mode = True
