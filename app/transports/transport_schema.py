from pydantic import BaseModel

class BalanceResponse(BaseModel):
    balance: float

class RechargeRequest(BaseModel):
    id: str
    value: float

class RechargeResponse(BaseModel):
    id: str
    previous_balance: float
    current_balance: float