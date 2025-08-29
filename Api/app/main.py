from fastapi import FastAPI, Depends
from routes.get_user import user_get
from routes.post_user import user_post
app = FastAPI()


app.include_router(user_get)
app.include_router(user_post)


@app.get("/")
def read_root():
    return {"message": "El servidor está funcionando correctamente 🚀"}

