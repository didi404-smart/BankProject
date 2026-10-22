from src.file_readers import read_file_csv, read_file_excel
from src.generators import filter_by_currency
from src.operations_analysis import process_bank_search
from src.processing import filter_by_state, sort_by_date
from src.utils import load_transactions_json
from src.widget import get_date, mask_account_card

STATUSES = {"EXECUTED", "CANCELED", "PENDING"}


def ask_menu_choice() -> str:
    print(
        "Привет! Добро пожаловать в программу работы \n"
        "с банковскими транзакциями. \n"
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла"
    )
    while True:
        choice = input().strip()
        if choice in ("1", "2", "3"):
            return choice
        print("Выбирите 1, 2 или 3")


def ask_status():
    print("Программа: Введите статус, по которому необходимо выполнить фильтрацию.")
    print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
    while True:
        state = input().strip().upper()
        if state in STATUSES:
            return state
        print(f"Статус {state} недоступен. Пожалуйста, выберите: EXECUTED, CANCELED или PENDING")


def ask_yes_no(prompt):
    while True:
        answer = input(prompt + " ").strip().lower()
        if answer in ("да", "yes", "y"):
            return True
        if answer in ("нет", "no", "n"):
            return False
        print("Введите Да или Нет.")


def ask_sort_order():
    while True:
        answer = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
        if answer in ("по возрастанию", "возрастанию"):
            return False
        if answer in ("по убыванию", "убыванию"):
            return True
        print('Введите "по возрастанию" или "по убыванию".')


def main():
    choice = ask_menu_choice()
    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        data = load_transactions_json("data/operations.json")
    elif choice == "2":
        print("Для обработки выбран CSV-файл.")
        data = read_file_csv("data/transactions.csv")
    elif choice == "3":
        print("Для обработки выбран XLSX-файл.")
        data = read_file_excel("data/transactions_excel.xlsx")
    state = ask_status()
    print(f'Операции отфильтрованы по статусу "{state}"')
    data = filter_by_state(data, state)
    if ask_yes_no("Отсортировать операции по дате? Да/Нет"):
        ans = ask_sort_order()
        data = sort_by_date(data, ans)
    if ask_yes_no("Выводить только рублевые транзакции? Да/Нет"):
        data = list(filter_by_currency(data, "RUB"))
    if ask_yes_no("Отфильтровать список транзакций по определенному слову в описании? Да/Нет"):
        word = input("Введите слово для фильтрации: ").strip()
        data = process_bank_search(data, word)
    if not data:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации\n")
        return
    print("Распечатываю итоговый список транзакций...\n")
    print(f"Всего банковских операций в выборке: {len(data)}")
    for operation in data:
        date = get_date(operation.get("date", ""))
        des = operation.get("description", "")
        from_str = mask_account_card(operation.get("from", ""))
        to_str = mask_account_card(operation.get("to", ""))
        amount = operation.get("operationAmount", {}).get("amount")
        code = operation.get("operationAmount", {}).get("currency", {}).get("code")
        if amount is None:
            amount = operation.get("amount", "")
        if code is None:
            code = operation.get("currency_code", "")
        print(f"{date} {des}")
        if from_str and to_str:
            print(f"{from_str} -> {to_str}")
        print(f"Сумма: {amount} {code}")


if __name__ == "__main__":
    main()
