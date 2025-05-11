import uuid
from datetime import datetime

from sqlalchemy.orm import Session
from app.users.user_model import User
from app.documents.document_model import Document
from app.transports.transport_model import TransportPass

def create_mock_data(db: Session):
    user = User(
        username="mock_user_um",
        email="mock_user_um@example.com",
        hashed_password="hashed_password"
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    cpf_document = Document(
        id=str(uuid.uuid4()),
        document_type="CPF",
        document_value={
            "full_name": "Usuario 1",
            "document_number":"123.456.789-00",
            "cpf_url":"https://example.com/cpf.pdf"
        },
        user_username="mock_user_um",
        alteration_date=datetime.now().isoformat()
    )
    rg_document = Document(
        id=str(uuid.uuid4()),
        document_type="RG",
        document_value={
            "full_name": "Usuario 1",
            "document_number":"12.345.678-9",
            "rg_url":"https://example.com/rg.pdf",
            "emission_date":"2025-05-03"
        },
        user_username="mock_user_um",
        alteration_date=datetime.now().isoformat()
    )
    vaccine_document = Document(
        id=str(uuid.uuid4()),
        document_type="VACCINE",
        document_value={
            "vaccine_name": "ASTRA",
            "vaccine_type": "COVID",
            "vaccine_url": "https://example.com/vaccine.pdf",
            "dose": "segunda"
        },
        user_username="mock_user_um",
        alteration_date=datetime.now().isoformat()
    )

    documents = [cpf_document, rg_document, vaccine_document]
    db.add_all(documents)
    db.commit()

    transport_pass = TransportPass(
        id=str(uuid.uuid4()),
        balance=50,
        username="mock_user_um"
    )
    db.add(transport_pass)
    db.commit()
    print("Dados mockados inseridos com sucesso!")
