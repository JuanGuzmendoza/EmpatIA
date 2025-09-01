from fastapi import FastAPI, Depends
from routes.Users import user
from routes.docs_users import google_docs
from routes.login import login

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # O pon la URL de tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user, prefix="/users", tags=["Users"])
app.include_router(google_docs, prefix="/google-docs", tags=["GoogleDocs"])
app.include_router(login, prefix="/auth", tags=["Auth"])

@app.get("/")
def read_root():
    return {"message": "El servidor está funcionando correctamente 🚀"}