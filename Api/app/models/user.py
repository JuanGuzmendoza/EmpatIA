from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)  # PK
    name = Column(String(50), nullable=False)  # nombre (short name)
    identification = Column(String(20), unique=True, index=True, nullable=False)  # identificación
    full_name = Column(String(100), nullable=False)  # nombre_completo
    age = Column(Integer, nullable=False)  # edad
    address = Column(String(200), nullable=True)  # dirección
    gender = Column(String(10), nullable=True)  # género
    psychological_history = Column(Text, nullable=True)  # historial_psicologico
    risk_status = Column(String(50), nullable=True)  # estado_de_riesgo
