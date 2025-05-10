from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.users.user_repository import create_user, get_user_by_email, get_user_by_username
from app.users.user_schema import UserCreate
from fastapi import HTTPException

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def create_new_user(user: UserCreate, db: Session):
    db_user = get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    db_user = get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username já cadastrado")

    hashed_password = hash_password(user.password)
    return create_user(db, user.username, user.email, hashed_password)
