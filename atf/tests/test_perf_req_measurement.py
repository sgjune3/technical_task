from statistics import mean, stdev
from unittest.mock import patch

from pytest import fixture
from requests import Request

from atf.helpers.perf_req_measurement import PerfRequestMeasurement


@fixture
def perf_measurement():
    return PerfRequestMeasurement(Request("GET", "htt://test"))


def test_calculate_st_dev(perf_measurement):
    times = [0.1, 1, 0.7]
    perf_measurement._response_times = times
    assert perf_measurement.calculate_st_dev() == stdev(times)


def test_calculate_avg(perf_measurement):
    times = [0.1, 1, 0.7]
    perf_measurement._response_times = times
    assert perf_measurement.calculate_avg_response_time() == mean(times)


@patch("atf.helpers.perf_req_measurement.Session")
def test_execute_perf_req(mock, perf_measurement):
    mock().__enter__().send().elapsed.total_seconds.return_value = 1.12
    perf_measurement.execute_perf_req(1)
    assert 1.12 == perf_measurement._response_times[0]
    assert 1.12 == perf_measurement.calculate_avg_response_time()
    assert 0 == perf_measurement.calculate_st_dev()


