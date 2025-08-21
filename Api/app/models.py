from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id_user = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(45), nullable=True)
    telefono = Column(String(45), nullable=True)
    edad = Column(String(45), nullable=True)
    historial_clinico = Column(String(45), nullable=True)
