from fastapi import FastAPI
#from sqlalchemy.sql.functions import mode
from . import schemas, models
from .database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.post("/blog")
def create(blog: schemas.Blog):
    return blog

