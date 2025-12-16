from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn 

app = FastAPI()


@app.get("/blog")

def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"data": f"{limit} published blogs from db"}
    else:
        return {"data": f"{limit} blogs from db"}

@app.get("/blog/unpublished")
def unpublished():
    return {"data": "all unpublished data"}

@app.get("/blog/{id}")
def show(id: int):
    return {"data" : id}

@app.get("/blog/{id}/comments")
def comments(id: int, limit = 10):
    return {"data" : {"1", "2", "3"}}


class Blog(BaseModel):
    title: str
    body: str
    year: int
    published: Optional[bool] = True


@app.post("/blog")
def create_blog(blog: Blog):
    
    return {"data" :f"Blog is created with book title {blog.title}"}



