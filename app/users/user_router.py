from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.users.user_schema import UserCreate
from app.users.user_service import UserService

router = APIRouter()

@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return UserService.create_new_user(user, db)