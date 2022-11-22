import json
from abc import ABC, abstractmethod
from pathlib import Path


class FileReader(ABC):

    @staticmethod
    @abstractmethod
    def read_file(file_path: Path):
        pass


class JsonFileReader(FileReader):
    """
    Class responsible for reading json files
    """

    @staticmethod
    def read_file(file_path: Path) -> dict:
        """
        Read json file
        :param file_path: path to the json file
        :return: dict
        """
        with open(file_path) as f:
            return json.load(f)
