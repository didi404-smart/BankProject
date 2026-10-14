from src.operations_analysis import process_bank_operations, process_bank_search


def test_process_bank_search(test_generators_1):
    res = process_bank_search(test_generators_1, "Оплата")
    assert res == [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2019-01-01T00:00:00.000000",
            "operationAmount": {"amount": "100.00", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Оплата",
            "from": "Счет 111",
            "to": "Счет 222",
        }
    ]


def test_process_bank_operations(test_generators_1):
    res = process_bank_operations(test_generators_1, ["Оплата", "Перевод организации"])
    assert res == {"Оплата": 1, "Перевод организации": 1}
