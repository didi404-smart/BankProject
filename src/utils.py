import json
import logging
from json import JSONDecodeError

from src.external_api import get_convert_to_rub

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("logs/utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def load_transactions_json(path):
    """принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, "r", encoding="utf-8") as file_json:
            data = json.load(file_json)
        if isinstance(data, list):
            logger.info("Приняли ваш файл, возвращаем список словарей с транзакциями")
            return data
        else:
            logger.info("Пустой файл")
            return []
    except FileNotFoundError:
        logger.error("Не удалось найти файл, попробуйте снова")
        return []
    except JSONDecodeError:
        logger.error("Файл содержит неправильный формат")
        return []


def transactions_amount_rub(transactions: dict) -> float:
    """Возвращает сумму транзакции в рублях"""
    code = transactions["operationAmount"]["currency"]["code"]
    amount = transactions["operationAmount"]["amount"]
    if code in ("USD", "EUR"):
        logger.info("Операция была в другой валюте, возвращаем сумму в рублях")
        return get_convert_to_rub(code, amount)
    if code == "RUB":
        logger.info("Операция была в рублях, возвращаем сумму транзакции")
        return float(amount)
    logger.error("Неккоректная валюта")
    raise ValueError(f"Unsupported currency: {code}")
