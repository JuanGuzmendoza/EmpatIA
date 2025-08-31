from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.db.db import get_db
from models.user import User
from schemas.user import UserBase, UserCreate, UserResponse as UserSchema
from typing import List

user = APIRouter()


@user.get(
    "/users",
    tags=["Users"],
    response_model=List[UserSchema],
    description="Get a list of all registered users"
)
def get_users(basededatos: Session = Depends(get_db)):
    return basededatos.query(User).all()

@user.post(
    "/users",
    tags=["Users"],
    response_model=UserSchema,  # <- salida (UserResponse)
    description="Create a new user in all registered users list"
)
def create_users(user_data: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        full_name=user_data.full_name,
        username=user_data.username,
        email=user_data.email,
        password_user=user_data.password_user,  # ahora sí existe
        national_id=user_data.national_id,
        age=user_data.age,
        id_genre=user_data.id_genre,
        country=user_data.country,
        city=user_data.city,
        phone=user_data.phone,
        emergency_contact=user_data.emergency_contact,
        address=user_data.address,
        user_profile=user_data.user_profile
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
