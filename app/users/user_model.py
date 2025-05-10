from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    username = Column(String, unique=True, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    documents = relationship("Document", back_populates="user")