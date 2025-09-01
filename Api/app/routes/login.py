from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.db.db import get_db
from models.user import User

login = APIRouter()

@login.post(
    "/login",
    tags=["Auth"],
    description="Login with email and password"
)
def login_user(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user or user.password_user != password:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return {
        "message": "Login exitoso",
        "user_id": user.id_user
    }