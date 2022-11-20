from pathlib import Path

from pytest import raises

from atf.helpers.api_model_factory import ApiModelFactory
from atf.helpers.file_reader import JsonFileReader
from atf.models.error_msg import ErrorMsg
from atf.models.people import People
from atf.models.planets import Planets
from atf.models.starships import Starships
from atf.models.validation_error_msg import ValidationErrorMsg

starship_data = JsonFileReader.read_file(Path.joinpath(Path(__file__).resolve().parent, "test_data",
                                                       "test_starships.json"))

people_data = JsonFileReader.read_file(Path.joinpath(Path(__file__).resolve().parent, "test_data",
                                                     "test_people.json"))

planets_data = JsonFileReader.read_file(Path.joinpath(Path(__file__).resolve().parent, "test_data",
                                                      "test_planets.json"))

err_msg_data = JsonFileReader.read_file(Path.joinpath(Path(__file__).resolve().parent, "test_data",
                                                      "test_err_msg.json"))

val_err_msg_data = JsonFileReader.read_file(Path.joinpath(Path(__file__).resolve().parent, "test_data",
                                                          "test_value_err_msg.json"))


def test_create_model_lower_case():
    model_factory = ApiModelFactory("starships")
    actual_model = model_factory.create_model(**starship_data)
    expected_model = Starships(**starship_data)
    assert actual_model == expected_model


def test_create_starship_model():
    model_factory = ApiModelFactory("STARSHIPS")
    actual_model = model_factory.create_model(**starship_data)
    expected_model = Starships(**starship_data)
    assert actual_model == expected_model


def test_unsupported_model():
    model = "ABC"
    with raises(ValueError, match=f'Unsupported model: {model}'):
        model_factory = ApiModelFactory(model)
        model_factory.create_model()


def test_create_people_model():
    model_factory = ApiModelFactory("PEOPLE")
    actual_model = model_factory.create_model(**people_data)
    expected_model = People(**people_data)
    assert actual_model == expected_model


def test_create_planets_model():
    model_factory = ApiModelFactory("PLANETS")
    actual_model = model_factory.create_model(**planets_data)
    expected_model = Planets(**planets_data)
    assert actual_model == expected_model


def test_create_err_msg_model():
    model_factory = ApiModelFactory("ERROR_MSG")
    actual_model = model_factory.create_model(**err_msg_data)
    expected_model = ErrorMsg(**err_msg_data)
    assert actual_model == expected_model


def test_create_val_err_msg_model():
    model_factory = ApiModelFactory("VALIDATION_ERR_MSG")
    actual_model = model_factory.create_model(**val_err_msg_data)
    expected_model = ValidationErrorMsg(**val_err_msg_data)
    assert actual_model == expected_model
