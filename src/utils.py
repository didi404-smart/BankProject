import json
from json import JSONDecodeError

from src.external_api import get_convert_to_rub


def load_transactions_json(path):
    try:
        with open(path, "r", encoding="utf-8") as file_json:
            data = json.load(file_json)
        if isinstance(data, list):
            return data
        else:
            return []
    except FileNotFoundError:
        return []
    except JSONDecodeError:
        return []


def transactions_amount_rub(transactions: dict) -> float:
    code = transactions["operationAmount"]["currency"]["code"]
    amount = transactions["operationAmount"]["amount"]
    if code in ("USD", "EUR"):
        return get_convert_to_rub(code, amount)
    if code == "RUB":
        return float(amount)
    raise ValueError(f"Unsupported currency: {code}")
