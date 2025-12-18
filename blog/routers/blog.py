from fastapi import APIRouter
from .. import schemas, models, database    
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from fastapi import Depends, status, Response, HTTPException
from .. import hashing
from ..repository import blog

router = APIRouter(
    tags=["blogs"],
    prefix = "/blog"
)


@router.get("/", response_model=list[schemas.ShowBlog])
def all(db: Session = Depends(get_db)):
    return blog.get_all(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_blog(request : schemas.Blog, db: Session = Depends(get_db)):
    return blog.create(request, db)




@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db)):
    return blog.delete(id, db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update(id, request, db)



@router.get("/blog/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id: int, response: Response, db: Session = Depends(get_db)):
    return blog.show(id, response, db)




