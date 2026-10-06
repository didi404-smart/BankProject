import json

from src.utils import load_transactions_json

def test_load_transactions_json_1(tmp_path):
    path = tmp_path / "ops.json"
    data = [{"id": 1}, {"id": 6}]
    path.write_text(json.dumps(data), encoding='utf-8')
    assert load_transactions_json(str(path)) == data

def test_load_transactions_json_2(tmp_path):
    path = tmp_path / "ops.json"
    path.write_text(json.dumps({"id": 1}), encoding='utf-8')
    assert load_transactions_json(str(path)) == []

def test_load_transactions_json_3(tmp_path):
    assert load_transactions_json("no_file.json") == []

def test_load_transactions_json_4(tmp_path):
    path = tmp_path / "ops.json"
    path.write_text("{'id': 1", encoding='utf-8')
    assert load_transactions_json(str(path)) == []