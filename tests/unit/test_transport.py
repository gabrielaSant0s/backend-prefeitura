from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app
from app.transports.transport_schema import BalanceResponse, RechargeResponse

client = TestClient(app)


def test_get_my_balance():
    with patch("app.transports.transport_repository.TransportRepository.get_balance") as mock_get_balance:
        mock_get_balance.return_value = BalanceResponse(balance=100)

        response = client.get("/transport/123")
        assert response.status_code == 200
        assert response.json() == {"balance": 100}
        mock_get_balance.assert_called_once()


def test_update_balance():
    with patch("app.transports.transport_repository.TransportRepository.update_balance") as mock_update_balance:
        mock_update_balance.return_value = RechargeResponse(
            id="123", current_balance=200.0, previous_balance=100.0
        )

        response = client.put("/transport/123", params={"valor": 100.0})
        assert response.status_code == 200
        assert response.json() == {
            "id": "123",
            "current_balance": 200.0,
            "previous_balance": 100.0
        }
        mock_update_balance.assert_called_once()
