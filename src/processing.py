def filter_by_state(list_dictionary: list[dict], status: str = "EXECUTED") -> list[dict]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению."""
    new_list_dictionary = []
    for dictionary in list_dictionary:
        if dictionary["state"] == status:
            new_list_dictionary.append(dictionary)
    return new_list_dictionary


def sort_by_date(list_dictionary: list[dict], is_value: bool = True) -> list[dict]:
    """Функция, которая возвращает список словарей, сортированных по дате"""
    list_dictionary.sort(key=lambda x: x["date"])
    if is_value:
        return list_dictionary[::-1]
    else:
        return list_dictionary
