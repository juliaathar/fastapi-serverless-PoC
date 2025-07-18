from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..crud import user_crud
from ..schemas import user_schema
from ..database import get_db
from app.schemas.user_schema import User

router = APIRouter(
    prefix="/users", 
    tags=["users"],  
)

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user_endpoint(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Já existe usuário com esse email")
    return user_crud.create_user(db=db, user=user)

@router.get("/{user_id}", response_model=user_schema.User)
def read_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    db_user = user_crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db_user

@router.get("/", response_model=List[user_schema.User])
def read_users_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = user_crud.get_users(db, skip=skip, limit=limit)
    return users

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    success = user_crud.delete_user(db, user_id=user_id)
    if not success:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"message": "Usuário deletado com sucesso"}
