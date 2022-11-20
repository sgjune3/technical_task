from random import randrange
from functools import wraps
from time import sleep
from typing import Dict, Tuple

from pydantic import BaseModel

from rest_api.data_generator import DataGenerator


def get_api_data(data_generator: DataGenerator) -> Dict[int, BaseModel]:
    """
    :param data_generator: *DataGenerator* used for generating data
    :return: dict with *int* id as key and *BaseModel* as value
    """
    return data_generator.generate_data()


def random_slow_down(rand_range: Tuple[int, int]):
    """
    Wait a random amount of milliseconds before the execution of a decorated function
    :param rand_range: *tuple* range from which a random value is chosen
    :return:
    """
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time_to_wait = randrange(*rand_range) / 1000
            sleep(time_to_wait)
            return func(*args, **kwargs)
        return wrapper
    return inner
