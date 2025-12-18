from fastapi import APIRouter, status, Depends, HTTPException 
from .. import schemas
from ..database import get_db
from sqlalchemy.orm import Session  
from ..repository import user
from .. import hashing
from .. import token
from .. import models



router = APIRouter(
    tags=["authentication"],
    prefix = "/login"
)

@router.post("/", status_code=status.HTTP_200_OK)
def login(request: schemas.Login, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"invalid credentials")
    if not hashing.Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"invalid credentials")
    access_token = token.create_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

