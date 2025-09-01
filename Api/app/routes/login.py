from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.db.db import get_db
from models.user import User
from schemas.login import RegistroCompleto 
from services.google_docs import createDocIaFirstTime

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
    

@login.post("/registerUser")
async def registro_completo(payload: RegistroCompleto, db: Session = Depends(get_db)):
    user_data = payload.user
    inscripcion_data = payload.inscripcion

    print("USER DATA:", user_data)
    print("INSCRIPCION DATA:", inscripcion_data)

    # --- Validación username duplicado ---
    if db.query(User).filter(User.username == user_data.get("username")).first():
        raise HTTPException(status_code=400, detail="El username ya está registrado")

    # --- 1. Crear documento / impresión clínica ---
    try:
        doc_response = createDocIaFirstTime(
            doc_number=int(user_data.get("national_id")),
            inscripcion_data=inscripcion_data
        )
        user_data["user_profile"] = doc_response["documentId"]
    except Exception as e:
        print("Error creando Google Docs + IA:", e)
        raise HTTPException(status_code=500, detail=f"No se pudo crear el documento: {str(e)}")

    # --- 2. Crear usuario en la base de datos ---
    try:
        new_user = User(**user_data)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except Exception as e:
        print("Error creando usuario en DB:", e)
        raise HTTPException(status_code=500, detail=f"No se pudo crear el usuario: {str(e)}")

    return {
        "message": "Usuario, inscripción e impresión clínica registrados correctamente",
        "user_id": new_user.id_user,
        "user_profile_doc_id": new_user.user_profile,
    }




