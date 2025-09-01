# schemas/registro.py
from pydantic import BaseModel
from typing import Dict, Any

class RegistroCompleto(BaseModel):
    user: Dict[str, Any]
    inscripcion: Dict[str, Any]
