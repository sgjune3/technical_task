from typing import Dict

from pydantic import BaseModel

from rest_api.data_generator import DataGenerator


def get_api_data(data_generator: DataGenerator) -> Dict[int, BaseModel]:
    """
    :param data_generator: *DataGenerator* used for generating data
    :return: dict with *int* id as key and *BaseModel* as value
    """
    return data_generator.generate_data()
