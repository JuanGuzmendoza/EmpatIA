from fastapi import FastAPI, Depends
from routes.Users import user
from routes.docs_users import google_docs
app = FastAPI()

app.include_router(user, prefix="/users", tags=["Users"])
app.include_router(google_docs, prefix="/google-docs", tags=["GoogleDocs"])

@app.get("/")
def read_root():
    return {"message": "El servidor está funcionando correctamente 🚀"}

