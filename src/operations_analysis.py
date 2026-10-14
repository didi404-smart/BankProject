import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка"""
    pattern = re.compile(re.escape(search), flags=re.IGNORECASE)
    result = []
    for operation in data:
        description = operation.get("description", "")
        if pattern.search(description):
            result.append(operation)
    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Принимает список словарей с данными о банковских операциях и список категорий операций, а возвращает словарь,
    в котором ключи — это названия категорий, а значения — это количество операций в каждой категории."""
    description = []
    categories_set = set(categories)
    for operation in data:
        key = operation.get("description")
        if key in categories_set:
            description.append(key)
    counts = Counter(description)
    return {cat: counts.get(cat, 0) for cat in categories}
