from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.users.user_repository import UserRepository
from app.users.user_schema import UserCreate
from fastapi import HTTPException

class UserService:
    @staticmethod
    def create_new_user(user: UserCreate, db: Session):
        db_user = UserRepository.get_user_by_email(db, user.email)
        if db_user:
            raise HTTPException(status_code=400, detail="Email já cadastrado")

        db_user = UserRepository.get_user_by_username(db, user.username)
        if db_user:
            raise HTTPException(status_code=400, detail="Username já cadastrado")

        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        hashed_password = pwd_context.hash(user.password)
        return UserRepository.create_user(db, user.username, user.email, hashed_password)
