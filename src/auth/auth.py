from datetime import timedelta, datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from starlette import status
from sqlalchemy.util import deprecated
from src.database.session import SessionLocal
from src.models.user import User
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from src.database.session import get_db
from jose import jwt, JWTError
import os

from src.schema.user import UserCreate, UserAuth

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

SECRET_KEY = os.getenv('JWT_SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
ouauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@router.post("/", status_code=status.HTTP_201_CREATED)
async def auth(db: db_dependency, create_user_request: UserAuth):
    create_user_model = User(
        email = create_user_request.email,
        password = bcrypt_context.hash(create_user_request.password)
    )

    db.add(create_user_model)
    db.commit()
