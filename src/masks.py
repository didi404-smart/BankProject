import logging

logger = logging.getLogger("masks")
file_handler = logging.FileHandler("logs/masks.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(number_card: str) -> str:
    """принимает на вход номер карты и возвращает ее маску"""
    if len(number_card) != 16 or not number_card.isdigit():
        logger.info("Неккоректный номер карты")
        return ""
    logger.info("Номер карты принят, создаем маску")
    answer = number_card[:4] + " "
    answer += number_card[4:6] + "** "
    answer += "**** " + number_card[-4:]
    logger.info("Возращаем маску номера карты")
    return answer


def get_mask_account(mask: str) -> str:
    """принимает на вход номер счета и возвращает его маску"""
    if len(mask) != 20 or not mask.isdigit():
        logger.info("Неккоректный номер счета")
        return ""
    logger.info("Номер счета принят, возвращаем маску")
    return "**" + mask[-4:]
