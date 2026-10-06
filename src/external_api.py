import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api.apilayer.com/exchangerates_data/convert"


def get_convert_to_rub(currency_code: str, amount: float) -> float:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise RuntimeError("API_KEY is not set")
    headers = {"apikey": api_key}
    params = {"from": currency_code, "to": "RUB", "amount": amount}
    response = requests.get(API_URL, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()
    return float(data["result"])
