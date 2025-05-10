from pydantic import BaseModel, Field
from typing import Dict, Any, Optional, Literal
from datetime import datetime

class CPFDocumentValue(BaseModel):
    full_name: str
    document_number: str
    cpf_url: str

class RGDocumentValue(BaseModel):
    full_name: str
    document_number: str
    rg_url: str
    emission_date: Optional[datetime] = None

class VaccineDocumentValue(BaseModel):
    vaccine_name: str
    vaccine_type: str
    vaccine_url: str
    dose: Optional[str] = None

class DocumentCreate(BaseModel):
    document_type: Literal['CPF', 'RG', 'VACCINE'] = Field(
        ...,
        example="CPF"
    )
    document_value: Dict[str, Any] = Field(
        ...,
        example={
            "full_name": "Gabriela Motta",
            "document_number": "12345678909",
            "cpf_url": "https://example.com/cpf.pdf"
        }
    )

class DocumentResponse(BaseModel):
    id: str
    document_type: str
    document_value: Dict[str, Any]
    username: str
    alteration_date : str

    class Config:
        orm_mode = True
