from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.db import get_db  # la dependencia de db.py
from models.user import User
from schemas.user import UserBase, UserCreate, UserResponse as UserSchema
from typing import List

user_get = APIRouter()


@user_get.get(
    "/users",
    tags=["Users"],
    response_model=List[UserSchema],
    description="Get a list of all registered users"
)
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

