from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import os
from dotenv import load_dotenv
from sqlalchemy import text

load_dotenv()

# Obtener las credenciales desde las variables de entorno
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Crear la cadena de conexión usando las variables de entorno
SQLALCHEMY_DATABASE_URL = f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Crear la conexión con la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Crear una sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()


try:
    # Intentar ejecutar la consulta con text()
    result = session.execute(text("SHOW TABLES;"))
    tables = result.fetchall()
    
    print("Conexión exitosa a la base de datos. Tablas disponibles:")
    for table in tables:
        print(table)
except SQLAlchemyError as e:
    print(f"Error en la conexión: {e}")
finally:
    session.close()
