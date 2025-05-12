from sqlalchemy.orm import Session
from app.documents.document_model import Document
from datetime import datetime
import uuid

from app.documents.document_schema import DocumentResponse

class DocumentRepository:
    @staticmethod
    def create_document(db: Session, document_data: dict) -> DocumentResponse:
        doc_id = str(uuid.uuid4())
        document = Document(
            id=doc_id,
            document_type=document_data["document_type"],
            document_value=document_data["document_value"],
            user_username=document_data["user_username"],
            alteration_date=datetime.now().isoformat()
        )
        db.add(document)
        db.commit()
        db.refresh(document)
        return DocumentResponse(
            id=doc_id,
            document_type=document_data["document_type"],
            document_value=document_data["document_value"],
            username=document_data["user_username"],
            alteration_date=datetime.now().isoformat()
        )

    @staticmethod
    def get_user_documents(db: Session, username: str):
        return db.query(Document).filter(Document.user_username == username).all()
