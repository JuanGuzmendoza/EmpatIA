from sqlalchemy.orm import Session
from app.models import User
from app.database import SessionLocal

def get_all_users():
    session = SessionLocal()
    try:
        users = session.query(User).all()
        for user in users:
            print(user.nombre, user.telefono, user.edad)
    finally:
        session.close()

get_all_users()
