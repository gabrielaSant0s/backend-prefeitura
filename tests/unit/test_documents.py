from datetime import datetime
import uuid
from types import SimpleNamespace

from fastapi.testclient import TestClient
from unittest.mock import patch, Mock

from app.auth.auth_dependencies import get_current_user
from app.main import app
from app.documents.document_model import Document
from app.users.user_schema import UserCreate

client = TestClient(app)

def override_get_current_user():
    return SimpleNamespace(username="mock_user_test")

app.dependency_overrides[get_current_user] = override_get_current_user

def test_create_document():
    with patch("app.documents.document_repository.DocumentRepository.create_document") as mock_create_document:
        id_doc = str(uuid.uuid4())
        date = datetime.now().isoformat()

        expected_document = {
            "id": id_doc,
            "document_type": "CPF",
            "document_value": {
                "full_name": "Usuario Test",
                "document_number": "123.456.789-00",
                "cpf_url": "https://example.com/cpf.pdf"
            },
            "username": "mock_user_test",
            "alteration_date": date
        }

        mock_create_document.return_value = expected_document

        response = client.post("/documents", json={
            "document_type": "CPF",
            "document_value": {
                "full_name": "Usuario Test",
                "document_number": "123.456.789-00",
                "cpf_url": "https://example.com/cpf.pdf"
            }
        })

        assert response.status_code == 200
        assert response.json() == expected_document
        mock_create_document.assert_called_once()

def test_get_user_documents():
    with patch("app.documents.document_repository.DocumentRepository.get_user_documents", autospec=True) as mock_get_documents:
        id_doc = str(uuid.uuid4())
        date = datetime.now()

        expected_documents = [{
            "id": id_doc,
            "document_type": "CPF",
            "document_value": {
                "full_name": "Usuario Test",
                "document_number": "123.456.789-00",
                "cpf_url": "https://example.com/cpf.pdf"
            },
            "username": "mock_user_test",
            "alteration_date": date.isoformat()
        }]

        mock_get_documents.return_value = [Document(
            id=id_doc,
            document_type="CPF",
            document_value={
                "full_name": "Usuario Test",
                "document_number": "123.456.789-00",
                "cpf_url": "https://example.com/cpf.pdf"
            },
            user_username="mock_user_test",
            alteration_date=date
        )]

        response = client.get("/documents/me")
        assert response.status_code == 200
        assert response.json() == expected_documents
        mock_get_documents.assert_called_once()
