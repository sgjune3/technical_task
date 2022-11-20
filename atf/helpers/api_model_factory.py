from pydantic import BaseModel

from atf.models.error_msg import ErrorMsg
from atf.models.people import People
from atf.models.planets import Planets
from atf.models.starships import Starships
from atf.models.validation_error_msg import ValidationErrorMsg


class ApiModelFactory:
    """
    Class responsible for creating model objects
    """

    def __init__(self, model_name: str):
        self.model_name = model_name.upper()

    def create_model(self, **kwargs) -> BaseModel:
        """
        Create model factory
        :param kwargs: passed later to the model
        :raises: ValueError: when model is not supported
        :return: BaseModel
        """
        if self.model_name == "PEOPLE":
            return People(**kwargs)
        elif self.model_name == "PLANETS":
            return Planets(**kwargs)
        elif self.model_name == "STARSHIPS":
            return Starships(**kwargs)
        elif self.model_name == "ERROR_MSG":
            return ErrorMsg(**kwargs)
        elif self.model_name == "VALIDATION_ERR_MSG":
            return ValidationErrorMsg(**kwargs)
        else:
            raise ValueError(f"Unsupported model: {self.model_name}")
