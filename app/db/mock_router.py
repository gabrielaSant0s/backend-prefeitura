from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.mock_data import create_mock_data

router = APIRouter()

@router.post("/")
def post_mock(
    db: Session = Depends(get_db)
):
    return create_mock_data(db)