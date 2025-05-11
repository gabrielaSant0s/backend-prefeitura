from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.transports.transport_schema import BalanceResponse, RechargeResponse
from app.transports.transport_service import TransportService

router = APIRouter()

@router.get("/{id_pass}", response_model=BalanceResponse)
def get_my_balance(
        db: Session = Depends(get_db),
        id_pass: str = None,
        service: TransportService = Depends()
):
    return service.get_balance_by_id(db, id_pass)


@router.put("/{id_pass}", response_model=RechargeResponse)
def update_balance(
        db: Session = Depends(get_db),
        id_pass: str = None,
        valor: float = None,
        service: TransportService = Depends()
):
    return service.pass_recharge(db, id_pass, valor)
