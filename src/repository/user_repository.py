from sqlalchemy.orm import Session
from src.models.user import User
from src.schema.user import UserCreate

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: UserCreate):
        db_user = User(username=user.username, email=user.email, password=user.password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_user(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

    def get_user_by_email(self, email: str) -> User:
        return self.db.query(User).filter(User.email == email).first()

    def update_user(self, user_id: int, user: UserCreate):
        db_user = self.get_user(user_id)
        if db_user:
            db_user.username = user.username
            db_user.email = user.email
            db_user.password = user.password
            self.db.commit()
            self.db.refresh(db_user)
            return db_user
        return None

    def delete_user(self, user_id: int):
        db_user = self.get_user(user_id)
        if db_user:
            self.db.delete(db_user)
            self.db.commit()
            return True
        return False
