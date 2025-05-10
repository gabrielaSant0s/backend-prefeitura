from sqlalchemy import Column, String, JSON, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.database import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(String, primary_key=True, index=True)
    document_type = Column(String, nullable=False)
    document_value = Column(JSON, nullable=False)
    user_username = Column(String, ForeignKey("users.username"))
    alteration_date = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="documents")