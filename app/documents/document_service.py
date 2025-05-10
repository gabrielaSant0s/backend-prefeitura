from typing import List

from sqlalchemy.orm import Session
from app.documents.document_repository import DocumentRepository
from app.documents.document_schema import DocumentResponse


class DocumentService:
    @staticmethod
    def create_document(db: Session, document_data: dict):
        return DocumentRepository.create_document(db, document_data)

    @staticmethod
    def get_documents_by_user(db: Session, username: str) -> List[DocumentResponse]:
        documents = DocumentRepository.get_user_documents(db, username)

        return [
            DocumentResponse(
                id=document.id,
                document_type=document.document_type,
                document_value=document.document_value,
                username=document.user_username,
                alteration_date=document.alteration_date.isoformat()
            )
            for document in documents
        ]
