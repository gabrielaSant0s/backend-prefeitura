from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class TransportPass(Base):
    __tablename__ = "transport_pass"

    id = Column(String, primary_key=True, index=True)
    balance = Column(Float, default=0.0)
    username = Column(String, ForeignKey("users.username"), index=True)

    user = relationship("User", back_populates="transports")

