import csv

import pandas as pd


def read_file_csv(path: str) -> list[dict]:
    """Читает csv файл и возвращет список словарей"""
    try:
        with open(path, "r", encoding="utf-8") as file_csv:
            return list(csv.DictReader(file_csv, delimiter=";"))
    except FileNotFoundError:
        return []


def read_file_excel(path: str) -> list[dict]:
    """Читает excel файл и возвращает список словарей"""
    try:
        excel_data = pd.read_excel(path)
        return excel_data.to_dict(orient="records")
    except FileNotFoundError:
        return []
