| *** Settings ***   |
| Documentation      | GET /starships/{id} performance measure
| Resource           | ../../resource_files/common_resource.resource
| Suite Setup        | start_api
| Suite Teardown     | stop_api
| Test tags          | task_2

| *** Variables ***              |
| ${URL}                         | ${BASE_URL}/starships

| *** Test Cases *** |
| GET /starships/{id} existing starship performance
| ... | [Documentation]               | Measure GET /starships/{id} performanc |
|     | ${REQ}                        | create_request  | GET                  | ${URL}/1
|     | measure_endpoint_performance  | ${REQ}          |                      |