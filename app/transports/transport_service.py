from app.transports.transport_repository import TransportRepository
from app.transports.transport_schema import BalanceResponse, RechargeResponse
from sqlalchemy.orm import Session

class TransportService:
    @staticmethod
    def get_balance_by_id(db: Session, id_pass: str) -> BalanceResponse:
        return TransportRepository.get_balance(id_pass, db)

    @staticmethod
    def pass_recharge(db: Session, id_pass: str, value: float) -> RechargeResponse:
        return TransportRepository.update_balance(id_pass, value, db)