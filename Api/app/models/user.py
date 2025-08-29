from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id_user = Column(Integer, primary_key=True, index=True, autoincrement=True)
    full_name = Column(String(255), nullable=False)
    username = Column(String(255), unique=True, nullable=True)
    email = Column(String(255), unique=True, nullable=False)
    password_user = Column(String(255), nullable=False)
    national_id = Column(String(100), unique=True, nullable=False)
    age = Column(Integer, nullable=False)
    id_genre = Column(Integer, ForeignKey("genres.id_genre"), nullable=False)
    country = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    phone = Column(Integer, nullable=False)
    emergency_contact = Column(Integer, nullable=True)
    address = Column(String(255), nullable=True)
    user_profile = Column(String(255), unique=True, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relación opcional con la tabla genres
    genre = relationship("Genre", back_populates="users")
