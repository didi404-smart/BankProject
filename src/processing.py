def filter_by_state(list_dictionary: list[dict], status: str = "EXECUTED") -> list[dict]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению."""
    answer = []
    for dictionary in list_dictionary:
        if dictionary["state"] == status:
            answer.append(dictionary)
    return answer


def sort_by_date(list_dictionary: list[dict], value: bool = True) -> list[dict]:
    """Функция, которая возвращает список словарей, сортированных по дате"""
    list_dictionary.sort(key=lambda x: x["date"])
    if value:
        return list_dictionary[::-1]
    else:
        return list_dictionary
