from concurrent.futures import ThreadPoolExecutor, as_completed
from os import cpu_count
from time import monotonic
from statistics import mean, stdev
from typing import Generator, List

from requests import Request, Session, Response


class PerfRequestMeasurement:

    def __init__(self, request: Request, workers: int = cpu_count()):
        self._request = request
        self._workers = workers
        self._response_times = []

    def execute_perf_req(self, execution_time_s: int) -> None:
        """
        Execute multiple requests and collect response times
        :param execution_time_s: specify time of test execution
        :return: None
        """
        result = []
        with Session() as session:
            t_end = monotonic() + execution_time_s
            with ThreadPoolExecutor(max_workers=self._workers) as pool:
                while monotonic() < t_end:
                    futures = [pool.submit(session.send, self._request.prepare()) for _ in range(self._workers)]
                    result.extend(self.__gather_results(futures))
                self._response_times.extend(self.__normalize_elapsed_time(result))

    def calculate_avg_response_time(self) -> float:
        """
        Calculate avg/mean response time
        :return: avg response time as *float*
        """
        return mean(self._response_times)

    def calculate_st_dev(self) -> float:
        """
        Calculate standard deviation response time
        :return: standard deviation response time as *float*
        """
        return stdev(self._response_times)

    def __gather_results(self, futures: list) -> Generator:
        """
        Gather future results
        :param futures: *list*
        :return: Generator
        """
        return (future.result() for future in as_completed(futures))

    def __normalize_elapsed_time(self, responses: List[Response]) -> Generator:
        """
        Convert elapsed times(timedelta) to seconds
        :param responses: *list*
        :return: Generator
        """
        return (response.elapsed.total_seconds() for response in responses)
