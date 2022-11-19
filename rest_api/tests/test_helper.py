from pathlib import Path

from rest_api.data_generator import PlanetsDataGenerator
from rest_api.helper import get_api_data
from rest_api.tests.helper import create_planets_model


def test_get_api_data():
    api_data = get_api_data(
        PlanetsDataGenerator(Path.joinpath(Path(__file__).resolve().parent, "test_data", "test_planets.json"))
    )
    assert len(api_data) == 100
    for i in range(100):
        assert api_data[i] == create_planets_model()
