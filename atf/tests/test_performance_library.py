import logging

from unittest.mock import patch

from requests import Request

from pytest import fixture

from atf.libraries.PerformanceLibrary import PerformanceLibrary


@fixture
def performance_library():
    return PerformanceLibrary()


@patch("atf.helpers.perf_req_measurement.Session")
def test_measure_endpoint_performance(mock, caplog, performance_library):
    caplog.set_level(logging.INFO)
    req = Request(method="GET", url="http://test.com")
    mock().__enter__().send().elapsed.total_seconds.return_value = 1.12
    performance_library.measure_endpoint_performance(req, 1)
    assert "Endpoint: http://test.com" in caplog.text
    assert "AVG response time (seconds):1.12" in caplog.text
    assert "ST DEV response time (seconds):0.0" in caplog.text
