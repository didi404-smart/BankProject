def mask_account_card(card: str) -> str:
    """Функция, которая возвращает строку с замаскированным номером"""
    if card[:4] != "Счет":
        number_card = card[-16:]
        answer = number_card[:4] + " "
        answer += number_card[4:6] + "** "
        answer += "**** " + number_card[-4:]
        return  card[:-16] + answer
    else:
        return card[:4] + " **" + card[-4:]

def get_date(data: str) -> str:
    return data[8:10] +"." + data[5:7] + "." + data[:4]

print(get_date("2024-03-11T02:26:18.671407"))