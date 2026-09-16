def filter_by_state(list_dictionary: list[dict], status: str = 'EXECUTED') -> list[dict]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
state соответствует указанному значению."""
    answer = []
    for dictionary in list_dictionary:
        if dictionary["state"] == status: answer.append(dictionary)
    return answer

def sort_by_date(list_dictionary: list[dict]) -> list[dict]:
    list_dictionary.sort(key = lambda x: x["date"])
    return list_dictionary

