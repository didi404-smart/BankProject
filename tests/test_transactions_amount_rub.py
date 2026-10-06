from unittest.mock import patch

from src.utils import transactions_amount_rub
import pytest

def test_transactions_amount_rub_1():
    transaction = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
    }
    with patch("src.utils.get_convert_to_rub") as mock_convert:
        mock_convert.return_value = 950.0
        assert transactions_amount_rub(transaction) == 950.0
        mock_convert.assert_called_once_with("USD", "8221.37")


def test_transactions_amount_rub_2():
    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
    }
    assert transactions_amount_rub(transaction) == 31957.58

def test_transactions_amount_rub_3():
    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "GRF"}},
    }
    with pytest.raises(ValueError) as inf:
        transactions_amount_rub(transaction)

    assert "Unsupported currency: GRF" in str(inf)