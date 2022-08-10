from fastapi import FastAPI

from database import engine
import models
from config import settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

()
@app.get("/")
async def root():
    return {"message": "Hello World"}

