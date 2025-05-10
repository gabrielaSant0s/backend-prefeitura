from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.users.user_schema import UserCreate
from app.users.user_service import create_new_user

router = APIRouter()

@router.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_new_user(user, db)