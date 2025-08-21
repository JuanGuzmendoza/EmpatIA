from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import models, database, schemas
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Dependencia para la sesión de DB
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/usuarios/", response_model=list[schemas.UserSchema])
def read_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

