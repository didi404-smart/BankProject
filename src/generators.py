from typing import Iterator


def filter_by_currency(transactions: list[dict], currency_code: str) -> Iterator[dict]:
    """Генератор, которая принимает на вход список словарей, представляющих транзакции"""
    for transaction in transactions:
        if transaction:
            if transaction["operationAmount"]["currency"]["code"] == currency_code:
                yield transaction


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        if "description" in transaction:
            yield transaction["description"]


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    if start > 0 and end > 0:
        for number in range(start, end + 1):
            s = f"{number:016d}"
            yield f"{s[:4]} {s[4:8]} {s[8:12]} {s[12:16]}"
