from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card: str) -> str:
    """Функция, которая возвращает строку с замаскированным номером"""
    if card == "" or card == " ":
        return " "
    if card[:4] != "Счет":
        return card[:-16] + get_mask_card_number(card[-16:])
    else:
        return card[:5] + get_mask_account(card)


def get_date(data: str) -> str:
    return data[8:10] + "." + data[5:7] + "." + data[:4]
