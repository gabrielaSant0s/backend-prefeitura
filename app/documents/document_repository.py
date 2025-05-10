from sqlalchemy.orm import Session
from app.documents.document_model import Document
from datetime import datetime
import uuid

class DocumentRepository:
    @staticmethod
    def create_document(db: Session, document_data: dict):

        print("============ doc", document_data)
        document = Document(
            id=str(uuid.uuid4()),
            document_type=document_data["document_type"],
            document_value=document_data["document_value"],
            user_username=document_data["user_username"],
            alteration_date=datetime.now().isoformat()
        )
        db.add(document)
        db.commit()
        db.refresh(document)
        return document

    @staticmethod
    def get_user_documents(db: Session, username: str):
        return db.query(Document).filter(Document.user_username == username).all()
