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
    

@login.post("/registerUser" , tags=["Auth"], description="Register user, inscripcion and generate clinical impression with IA")
async def registro_completo(payload: RegistroCompleto, db: Session = Depends(get_db)):
    user_data = payload.user
    inscripcion_data = payload.inscripcion

    # Validación username duplicado
    if db.query(User).filter(User.username == user_data.get("username")).first():
        raise HTTPException(status_code=400, detail="El username ya está registrado")

    # Crear usuario
    new_user = User(**user_data)
    db.add(new_user)
    try:
        db.commit()
        db.refresh(new_user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    # Crear documento en Google Docs y actualizar con IA
    try:
        doc_response = createDocIaFirstTime(
            doc_number=int(user_data.get("national_id")), 
            inscripcion_data=inscripcion_data
        )
        new_user.user_profile = doc_response["documentId"]
        db.commit()
        db.refresh(new_user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {
        "message": "Usuario, inscripción e impresión clínica registrados correctamente",
        "user_id": new_user.id_user,
        "user_profile_doc_id": new_user.user_profile,
    }
