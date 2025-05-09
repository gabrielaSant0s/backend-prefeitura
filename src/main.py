from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from src.auth import auth
from src.service.user_service import UserService
from src.schema.user import UserCreate, UserResponse
from src.database.session import get_db

app = FastAPI()
app.include_router(auth.router)

@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.create_user(user)

@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.update_user(user_id, user)

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.delete_user(user_id)
