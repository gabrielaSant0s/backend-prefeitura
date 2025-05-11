from sqlalchemy.orm import Session
from app.transports.transport_model import TransportPass
from app.transports.transport_schema import BalanceResponse, RechargeResponse


class TransportRepository:
    @staticmethod
    def get_balance(id_pass: str, db: Session):
        data = db.query(TransportPass).filter(TransportPass.id == id_pass).first()
        return BalanceResponse(balance=data.balance)

    @staticmethod
    def update_balance(id_pass: str, value: float, db: Session):
        current_balance = db.query(TransportPass.balance).filter(TransportPass.id == id_pass).scalar()
        new_balance = value + current_balance
        db.query(TransportPass).filter(TransportPass.id == id_pass).update({"balance": new_balance})
        db.commit()
        return RechargeResponse(id=id_pass, current_balance=new_balance, previous_balance=current_balance)