from os import cpu_count

from requests import Request
from robot.api.deco import library
from robot.api import logger

from atf.helpers.perf_req_measurement import PerfRequestMeasurement


@library(scope='GLOBAL', version='1.00', auto_keywords=True)
class PerformanceLibrary:
    """Performance testing library"""

    def measure_endpoint_performance(self, request: Request, execution_time_s: int = 60,
                                     workers: int = cpu_count()) -> None:
        """
        Measure API performance triggering multiple requests for a specific time and calculating AVG/ST DEV
        :param request: Request object
        :param execution_time_s: specify time of test execution
        :param workers: number of requests executed simultaneously by default no cpu
        :return: None
        """
        perf_req_executor = PerfRequestMeasurement(request, workers)
        perf_req_executor.execute_perf_req(execution_time_s)
        avg = perf_req_executor.calculate_avg_response_time()
        st_dev = perf_req_executor.calculate_st_dev()
        msg = f"Endpoint: {request.url}\nAVG response time (seconds):{avg}\nST DEV response time (seconds):{st_dev}"
        logger.info(msg)
        logger.console(msg)
