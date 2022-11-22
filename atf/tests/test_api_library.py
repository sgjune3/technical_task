from multiprocessing import Process
from pathlib import Path
from unittest.mock import Mock, patch

from pydantic import ValidationError
from pytest import fixture, raises
from requests import Response, Request

from atf.configs.config import APP_NAME, LOG_INI, HOST, PORT
from atf.helpers.file_reader import JsonFileReader
from atf.libraries.ApiLibrary import ApiLibrary


@fixture
def api_library():
    return ApiLibrary()


test_err_msg_path = Path.joinpath(Path(__file__).resolve().parent, "test_data", "test_err_msg.json")


@patch("atf.libraries.ApiLibrary.Popen")
def test_start_api(mock, api_library):
    api_library._uvicorn_process = Mock(Process)
    api_library.start_api()
    mock.assert_called_with(["uvicorn", APP_NAME, "--host", HOST, "--port", PORT, "--log-config", LOG_INI])


def test_stop_api(api_library):
    api_library._uvicorn_process = Mock(Process)
    api_library.stop_api()
    api_library._uvicorn_process.kill.assert_called()


@patch("atf.libraries.ApiLibrary.Session")
def test_send_request(mock, api_library):
    return_value = Response()
    mock().__enter__().send.return_value = return_value
    resp = api_library.send_request("GET", "http://url")
    mock().__enter__().send.assert_called_once()
    assert resp == return_value
    assert mock().__enter__().send.call_args[0][0].__dict__["method"] == "GET"
    assert mock().__enter__().send.call_args[0][0].__dict__["url"] == "http://url/"


def test_verify_api_response_eq_values(api_library):
    json = JsonFileReader.read_file(test_err_msg_path)
    api_library.verify_api_response(json, "ERROR_MSG", test_err_msg_path)


def test_verify_api_response_neq_values(api_library):
    with raises(AssertionError, match="Actual model: detail='XYZ' != expected model: detail='detail'"):
        api_library.verify_api_response({"detail": "XYZ"}, "ERROR_MSG", test_err_msg_path)


def test_verify_api_response_different_models(api_library):
    with raises(ValidationError, match=r".*value is not a valid list.*"):
        api_library.verify_api_response({"detail": "XYZ"}, "VALIDATION_ERR_MSG", test_err_msg_path)


def test_create_request(api_library):
    expected_req = Request("GET", "http://test.com")
    actual_req = api_library.create_request("GET", "http://test.com")
    assert isinstance(actual_req, Request)
    assert actual_req.url == expected_req.url
    assert actual_req.method == expected_req.method
