import json
from pathlib import Path

from atf.helpers.file_reader import JsonFileReader


def test_json_file_reader(tmp_path):
    test_dict = {"abc": "test_val", "x": [1]}
    file_path = Path.joinpath(tmp_path, "test.json")
    with open(file_path, "w") as f:
        json.dump(test_dict, f)
    assert test_dict == JsonFileReader.read_file(file_path)
