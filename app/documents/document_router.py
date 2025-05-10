from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.documents.document_schema import DocumentCreate, DocumentResponse
from app.documents.document_service import DocumentService
from app.auth.auth_dependencies import get_current_user

router = APIRouter()

@router.post("/", response_model=DocumentResponse)
def create_document(
    document: DocumentCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    document_data ={}
    document_data["document_value"]= document.document_value
    document_data["user_username"] = current_user.username
    document_data["document_type"] = document.document_type
    db_document = DocumentService.create_document(db, document_data)
    return db_document

@router.get("/documents/me", response_model=list[DocumentResponse])
def get_my_documents(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    documents = DocumentService.get_documents_by_user(db, current_user.username)
    if not documents:
        raise HTTPException(status_code=404, detail="No documents found")
    return documents
