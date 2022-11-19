from pathlib import Path
from json import load
from typing import Dict
from abc import ABC, abstractmethod
from pydantic import BaseModel

from rest_api.models.people import People
from rest_api.models.planets import Planets
from rest_api.models.starships import Starships


class DataGenerator(ABC):

    def __init__(self, json_path: Path):
        self.json_path = json_path

    @abstractmethod
    def generate_data(self, nof_data_tb_generated: int = 100) -> Dict[int, BaseModel]:
        """
        Generate BaseModel data and return it as dictionary
        :param nof_data_tb_generated: number of data to be generated *by default 100*
        :return: dict with *int* id as key and *BaseModel* as value
        """

    def _read_json_file(self) -> dict:
        """
        Read json file and return it as dictionary
        :return: json represented as *dict*
        """
        with open(self.json_path) as f:
            return load(f)


class PeopleDataGenerator(DataGenerator):

    def generate_data(self, nof_data_tb_generated: int = 100) -> Dict[int, BaseModel]:
        return {i: People(**self._read_json_file()) for i in range(nof_data_tb_generated)}


class PlanetsDataGenerator(DataGenerator):

    def generate_data(self, nof_data_tb_generated: int = 100) -> Dict[int, BaseModel]:
        return {i: Planets(**self._read_json_file()) for i in range(nof_data_tb_generated)}


class StarshipsDataGenerator(DataGenerator):

    def generate_data(self, nof_data_tb_generated: int = 100) -> Dict[int, BaseModel]:
        return {i: Starships(**self._read_json_file()) for i in range(nof_data_tb_generated)}
