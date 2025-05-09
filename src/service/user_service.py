from sqlalchemy.orm import Session
from src.repository.user_repository import UserRepository
from src.schema.user import UserCreate, UserResponse
from fastapi import HTTPException

class UserService:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def create_user(self, user: UserCreate) -> UserResponse:
        db_user = self.repo.create_user(user)
        return UserResponse(id=db_user.id, username=db_user.username, email=db_user.email, password=db_user.password)

    def update_user(self, user_id: int, user: UserCreate) -> UserResponse:
        db_user = self.repo.update_user(user_id, user)
        if db_user:
            return UserResponse(id=db_user.id, username=db_user.username, email=db_user.email, password=db_user.password)
        raise HTTPException(status_code=404, detail="User not found")

    def delete_user(self, user_id: int) -> dict:
        if self.repo.delete_user(user_id):
            return {"detail": "User deleted successfully"}
        raise HTTPException(status_code=404, detail="User not found")
