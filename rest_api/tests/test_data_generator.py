from pathlib import Path
from pytest import fixture

from rest_api.data_generator import PeopleDataGenerator, PlanetsDataGenerator, StarshipsDataGenerator
from rest_api.tests.helper import create_people_model, create_planets_model, create_starships_model


@fixture
def people_data_generator():
    return PeopleDataGenerator(Path.joinpath(Path(__file__).resolve().parent, "test_data", "test_people.json"))


@fixture
def planets_data_generator():
    return PlanetsDataGenerator(Path.joinpath(Path(__file__).resolve().parent, "test_data", "test_planets.json"))


@fixture
def starships_data_generator():
    return StarshipsDataGenerator(Path.joinpath(Path(__file__).resolve().parent, "test_data", "test_starships.json"))


def test_generate_people_data_1_elem(people_data_generator):
    assert people_data_generator.generate_data(1) == {0: create_people_model()}


def test_generate_people_data_0_elem(people_data_generator):
    assert people_data_generator.generate_data(0) == {}


def test_generate_people_data(people_data_generator):
    generated_data = people_data_generator.generate_data()
    assert len(generated_data) == 100
    for i in range(100):
        assert generated_data[i] == create_people_model()


def test_generate_planets_data_1_elem(planets_data_generator):
    assert planets_data_generator.generate_data(1) == {0: create_planets_model()}


def test_generate_planets_data_0_elem(planets_data_generator):
    assert planets_data_generator.generate_data(0) == {}


def test_generate_planets_data(planets_data_generator):
    generated_data = planets_data_generator.generate_data()
    assert len(generated_data) == 100
    for i in range(100):
        assert generated_data[i] == create_planets_model()


def test_generate_starships_data_1_elem(starships_data_generator):
    assert starships_data_generator.generate_data(1) == {0: create_starships_model()}


def test_generate_starships_data_0_elem(starships_data_generator):
    assert starships_data_generator.generate_data(0) == {}


def test_generate_starships_data(starships_data_generator):
    generated_data = starships_data_generator.generate_data()
    assert len(generated_data) == 100
    for i in range(100):
        assert generated_data[i] == create_starships_model()
