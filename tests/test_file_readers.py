from unittest.mock import mock_open, patch

import pandas as pd

from src.file_readers import read_file_csv, read_file_excel


def test_file_read_csv():
    csv_text = "id;state\n1;EXECUTED\n2;CANCELED\n"
    with patch("src.file_readers.open", mock_open(read_data=csv_text)):
        res = read_file_csv("path.csv")

    assert res == [
        {"id": "1", "state": "EXECUTED"},
        {"id": "2", "state": "CANCELED"},
    ]


def test_read_file_csv_2():
    with patch("src.file_readers.open", side_effect=FileNotFoundError):
        res = read_file_csv("not.csv")
    assert res == []


def test_file_read_excel():
    fake_excel_file = pd.DataFrame([{"id": 1, "state": "EXECUTED"}, {"id": 2, "state": "CANCELED"}])
    with patch("src.file_readers.pd.read_excel", return_value=fake_excel_file) as mock_read_excel:
        res = read_file_excel("path.xlsx")
    assert res == [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
    ]
    mock_read_excel.assert_called_once_with("path.xlsx")


def test_file_read_excel_2():
    with patch("src.file_readers.pd.read_excel", side_effect=FileNotFoundError):
        res = read_file_excel("not.xlsx")
    assert res == []
