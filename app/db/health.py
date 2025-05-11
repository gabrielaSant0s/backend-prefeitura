from sqlalchemy import text
from sqlalchemy.orm import Session
from fastapi import APIRouter, status, HTTPException, Depends
from app.db.database import get_db

router = APIRouter()

@router.get("/", status_code=status.HTTP_200_OK)
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1")).fetchone()
        return {"status": "UP", "database": "Connected"}
    except Exception as e:
        print(f"Erro no health check: {str(e)}")
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Service Unavailable")
