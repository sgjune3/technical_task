| *** Settings ***   |
| Documentation      | GET /planets/{id} performance measure
| Resource           | ../../resource_files/common_resource.resource
| Suite Setup        | start_api
| Suite Teardown     | stop_api
| Test tags          | task_2

| *** Variables ***              |
| ${URL}                         | ${BASE_URL}/planets

| *** Test Cases *** |
| GET /planets/{id} existing person performance                   
| ... | [Documentation]               | Measure GET /planets/{id} performance|
|     | ${REQ}                        | create_request  | GET                | ${URL}/1
|     | measure_endpoint_performance  | ${REQ}          |                    |