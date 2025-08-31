from fastapi import FastAPI, Depends
from routes.user_routes import user
from routes.docs_users import google_docs
app = FastAPI()

app.include_router(user, prefix="/users", tags=["Users"])
app.include_router(google_docs, prefix="/google-docs", tags=["GoogleDocs"])