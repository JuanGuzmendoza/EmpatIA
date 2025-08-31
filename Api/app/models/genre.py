from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from config.db import Base

class Genre(Base):
    __tablename__ = "genres"

    id_genre = Column(Integer, primary_key=True, index=True, autoincrement=True)
    genre_type = Column(String(50), nullable=False)
    abbreviation = Column(String(10), nullable=False)

    users = relationship("User", back_populates="genre")