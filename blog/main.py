from fastapi import FastAPI
from . import models, schemas
from .database import engine


app = FastAPI()


models.Base.metadata.create_all(bind=engine)


@app.post("/blog")
def create_blog(request : schemas.Blog, db):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog