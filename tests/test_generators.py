import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_1(test_generators_1):
    generation = filter_by_currency(test_generators_1, "USD")
    assert next(generation) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }

    assert next(generation) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }

    with pytest.raises(StopIteration):
        next(generation)


def test_filter_by_currency_2(test_generators_1):
    generation = filter_by_currency(test_generators_1, "EUR")
    with pytest.raises(StopIteration):
        next(generation)


def test_filter_by_currency_3():
    generation = filter_by_currency([{}], "EUR")
    with pytest.raises(StopIteration):
        next(generation)


def test_transaction_descriptions_1(test_generators_1):
    generation = transaction_descriptions(test_generators_1)
    assert next(generation) == "Оплата"
    assert next(generation) == "Перевод организации"
    assert next(generation) == "Перевод со счета на счет"
    with pytest.raises(StopIteration):
        next(generation)


def test_transaction_descriptions_2():
    with pytest.raises(StopIteration):
        next(transaction_descriptions([{}]))


@pytest.mark.parametrize("start, end", [(1, 5)])
def test_card_number_generator(start, end):
    gener = card_number_generator(start, end)
    assert next(gener) == "0000 0000 0000 0001"
    assert next(gener) == "0000 0000 0000 0002"
    assert next(gener) == "0000 0000 0000 0003"
    assert next(gener) == "0000 0000 0000 0004"
    assert next(gener) == "0000 0000 0000 0005"


def test_card_number_generator_2():
    with pytest.raises(StopIteration):
        next(card_number_generator(-4, 10000))
