import csv
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def read_file_csv(path: str) -> list[dict]:
    """Читает csv файл и возвращет список словарей"""
    try:
        file_path = Path(path)
        if not file_path.is_absolute():
            file_path = PROJECT_ROOT / file_path
        with open(file_path, "r", encoding="utf-8") as file_csv:
            return list(csv.DictReader(file_csv, delimiter=";"))

    except FileNotFoundError:
        return []


def read_file_excel(path: str) -> list[dict]:
    """Читает excel файл и возвращает список словарей"""
    try:
        file_path = Path(path)
        if not file_path.is_absolute():
            file_path = PROJECT_ROOT / file_path
        excel_data = pd.read_excel(file_path)
        return excel_data.to_dict(orient="records")
    except FileNotFoundError:
        return []
