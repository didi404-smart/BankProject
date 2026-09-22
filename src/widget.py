from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card: str) -> str:
    """Функция, которая возвращает строку с замаскированным номером"""
    if (
        card == ""
        or card == " "
        or (card[:4] != "Счет" and (card[:-16] != "Visa Platinum " and card[:-16] != "Maestro "))
    ):
        return ""
    if card[:4] != "Счет":
        mask_card = get_mask_card_number(card[-16:])
        if mask_card != "":
            return card[:-16] + mask_card
        return ""
    else:
        mask_account = get_mask_account(card[5:])
        if mask_account != "":
            return card[:5] + mask_account
        return ""


def get_date(data: str) -> str:
    """Функция, которая форматирует дату"""
    if len(data) != 26:
        return ""
    day = data[8:10]
    month = data[5:7]
    year = data[:4]
    if day.isdigit() and month.isdigit() and year.isdigit() and data[4] == "-" and data[7] == "-":
        return day + "." + month + "." + year
    return ""
