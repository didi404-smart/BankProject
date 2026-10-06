def filter_by_state(list_of_dictionaries: list[dict], status: str = "EXECUTED") -> list[dict]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению."""
    new_list_of_dictionary = []
    for dictionary in list_of_dictionaries:
        if dictionary["state"] == status:
            new_list_of_dictionary.append(dictionary)
    return new_list_of_dictionary


def sort_by_date(list_of_dictionaries: list[dict], is_value: bool = True) -> list[dict]:
    """Функция, которая возвращает список словарей, сортированных по дате"""
    return sorted(list_of_dictionaries, key=lambda x: x["date"], reverse=is_value)
