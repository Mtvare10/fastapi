from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, models, hashing
from ..database import get_db
from sqlalchemy.orm import Session
from fastapi.responses import Response
from ..repository import user
from fastapi import Depends, status, HTTPException




router = APIRouter(
    tags=["users"],
    prefix = "/user"
)




@router.post("/", response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    
    return user.create(request, db)

@router.get("/{id}", response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_user(id, db)


    
