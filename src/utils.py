import json
from json import JSONDecodeError


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
