from fastapi import FastAPI, Depends
from routes.user_routes import user
app = FastAPI()


app.include_router(user)