from fastapi import FastAPI
from .db import engine
from . import models
from .routes import users, authentication

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
def root():
    return {'message':"welcome to fastapi platform"}

app.include_router(authentication.router)
app.include_router(users.router)