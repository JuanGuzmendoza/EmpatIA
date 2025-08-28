    # db.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from dotenv import load_dotenv


# Cargar variables del .env
load_dotenv()

# URL de la base de datos
DATABASE_URL = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

# Engine de SQLAlchemy
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Sesión local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos ORM
Base = declarative_base()

# =======================
# Dependencia para FastAPI
# =======================
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
