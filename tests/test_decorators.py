import pytest

from src.decorators import log


def test_decorators_1(capsys):
    @log()
    def add(x, y):
        return x + y

    res = add(1, 3)
    captured = capsys.readouterr()
    assert res == 4
    assert captured.out == "add ok\n"


def test_decorators_2(capsys):
    @log()
    def div(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        div(2, 0)
    captured = capsys.readouterr()
    assert captured.out == "div error: ZeroDivisionError: division by zero. Inputs: (2, 0), {}\n"


def test_decorators_file_1(tmp_path):
    log_file = tmp_path / "test_log.txt"

    @log(filename=str(log_file))
    def mul(x, y):
        return x * y

    assert mul(2, 6) == 12
    assert log_file.read_text(encoding="utf-8") == "mul ok"


def test_decorators_file_2(tmp_path):
    log_file = tmp_path / "test_log2.txt"

    @log(filename=str(log_file))
    def list_item(my_list, my_index):
        return my_list[my_index]

    with pytest.raises(IndexError):
        list_item([1, 2, 3, 4], 30)

    text_error = log_file.read_text(encoding="utf-8")
    assert text_error == "list_item error: IndexError: list index out of range. Inputs: ([1, 2, 3, 4], 30), {}"
