from ..database import get_db
from .. import models
from sqlalchemy.orm import Session
from .. import schemas
from fastapi import Depends, HTTPException, status
from fastapi.responses import Response



def get_all():
    blogs = db.query(models.Blog).all()
    return blogs


def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1 )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    if not blog:
        return {"detail": f"Blog with id {id} not found"}
    db.commit()
    return {"detail": f"Blog with id {id} deleted"}

def update(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).update(request)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    
    db.commit()
    return blog

def show(id: int, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"detail": f"Blog with id {id} not found"}
    return blog
