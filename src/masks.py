def get_mask_card_number(number_card: str) -> str:
    """принимает на вход номер карты и возвращает ее маску"""
    if len(number_card) != 16 or not number_card.isdigit():
        return ""
    answer = number_card[:4] + " "
    answer += number_card[4:6] + "** "
    answer += "**** " + number_card[-4:]
    return answer


def get_mask_account(mask: str) -> str:
    """принимает на вход номер счета и возвращает его маску"""
    if len(mask) != 20 or not mask.isdigit():
        return ""
    return "**" + mask[-4:]
