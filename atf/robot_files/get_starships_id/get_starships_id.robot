| *** Settings ***   |                                               |
| Documentation      | GET /starships/{id}                           |
| Resource           | ../../resource_files/common_resource.resource |
| Suite Setup        | start_api                                     |
| Suite Teardown     | stop_api                                      |
| Test tags          | task_1                                        | functional

| *** Variables ***              |
| ${URL}                         | ${BASE_URL}/starships
| ${JSON_FILE_SUCCESS_PATH}      | atf/robot_files/get_starships_id/get_starships_id_success.json
| ${JSON_FILE_NOT_FOUND_PATH}    | atf/robot_files/get_starships_id/get_starships_id_starship_not_found.json
| ${JSON_FILE_INCORRECT_ID_PATH} | atf/robot_files/get_starships_id/get_starships_id_incorrect_id.json

| *** Test Cases *** |
| GET /starships/{id} existing starship                   
| ... | [Documentation]               | API should return correct response when starship exists |           |
|     | ${RESP}                       | send_request                                            | GET       | ${URL}/0
|     | Response code should be equal | ${RESP}                                                 | 200       |
|     | verify_api_response           | ${RESP.json()}                                          | STARSHIPS | ${JSON_FILE_SUCCESS_PATH}

| GET /starships/{id} non-existing starship 
| ... | [Documentation]               | API should return err msg when starship doesn't exist |               |
|     | ${RESP}                       | send_request                                          | GET           | ${URL}/1000
|     | Response code should be equal | ${RESP}                                               | 404           |
|     | verify_api_response           | ${RESP.json()}                                        | ERROR_MSG     | ${JSON_FILE_NOT_FOUND_PATH}


| GET /starships/{id} incorrect id 
| ... | [Documentation]               | API should return err msg when provided id is incorrect |                     |
|     | ${RESP}                       | send_request                                            | GET                 |  ${URL}/X
|     | Response code should be equal | ${RESP}                                                 | 422                 |
|     | verify_api_response           | ${RESP.json()}                                          | VALIDATION_ERR_MSG  | ${JSON_FILE_INCORRECT_ID_PATH}