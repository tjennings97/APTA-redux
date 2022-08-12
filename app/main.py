from fastapi import Depends, FastAPI
import fastapi

from database import engine, get_db
import models
from config import settings
from routers import user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router) #include router object from user file, imports specific routes


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/test")
def test_route():
    return {"data"}