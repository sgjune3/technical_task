from pathlib import Path
from time import sleep
from subprocess import Popen

from requests import Session, Request, Response
from robot.api.deco import library

from atf.configs.config import APP_NAME, LOG_INI
from atf.helpers.api_model_factory import ApiModelFactory
from atf.helpers.file_reader import JsonFileReader


@library(scope='GLOBAL', version='1.00', auto_keywords=True)
class ApiLibrary:
    """
    API testing library
    """
    def __init__(self):
        self._uvicorn_process = None

    def send_request(self, http_method: str, url: str, headers=None, data=None, params=None, auth=None, cookies=None,
                     json=None) -> Response:
        """
        Send HTTP request and return response
        :param http_method: *required*
        :param url: *required*
        :param headers: by default None
        :param data: by default None
        :param params: by default None
        :param auth: by default None
        :param cookies: by default None
        :param json: by default None
        :return: Response object
        """
        with Session() as session:
            req = Request(method=http_method, url=url, headers=headers, data=data, params=params, auth=auth,
                          cookies=cookies, json=json)
            resp = session.send(req.prepare())
            return resp

    def verify_api_response(self, json_dict: dict, model: str, path_to_json_file: str) -> None:
        """
        Compare Json/API response with json file.
        :param json_dict: API response represented as json used for creating actual model
        :param model: pydantic model used for creating models
        :param path_to_json_file: path to the json file used for creating expected model
        :raises AssertionError: when current model is not equal expected model
        :return: None
        """
        model_factory = ApiModelFactory(model)
        actual_model = model_factory.create_model(**json_dict)
        expected_model = model_factory.create_model(**JsonFileReader.read_file(Path(path_to_json_file)))
        assert actual_model == expected_model, f"Actual model: {actual_model} != expected model: {expected_model}"

    def start_api(self) -> None:
        """
        Start uvicorn process and wait 1 s to be sure that api is ready
        :return: None
        """
        self._uvicorn_process = Popen(["uvicorn", APP_NAME, "--log-config", LOG_INI])
        sleep(1)

    def stop_api(self) -> None:
        """
        Kill uvicorn process
        :return: None
        """
        self._uvicorn_process.kill()
