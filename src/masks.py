def get_mask_card_number(number_card: str) -> str:
    """принимает на вход номер карты и возвращает ее маску"""
    answer = number_card[:4] + " "
    answer += number_card[4:6] + "** "
    answer += "**** " + number_card[-4:]
    return answer


def get_mask_account(mask: str) -> str:
    """принимает на вход номер счета и возвращает его маску"""
    return "**" + mask[-4:]
