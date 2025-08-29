from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime



Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    full_name = Column(String(255), nullable=False)
    username = Column(String(255), unique=True, nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phone = Column(Integer, nullable=True)
    address = Column(String(255), nullable=True)
    user_profile = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    update_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
