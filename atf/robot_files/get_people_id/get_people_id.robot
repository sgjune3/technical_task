| *** Settings ***   |
| Documentation      | GET /people/{id}
| Resource           | ../../resource_files/common_resource.resource
| Suite Setup        | start_api
| Suite Teardown     | stop_api
| Test tags          | task_1

| *** Variables ***              |
| ${URL}                         | ${BASE_URL}/people
| ${JSON_FILE_SUCCESS_PATH}      | atf/robot_files/get_people_id/get_people_id_success.json
| ${JSON_FILE_NOT_FOUND_PATH}    | atf/robot_files/get_people_id/get_people_id_person_not_found.json
| ${JSON_FILE_INCORRECT_ID_PATH} | atf/robot_files/get_people_id/get_people_id_incorrect_id.json

| *** Test Cases *** |
| GET /people/{id} existing person     |               
| ... |  [Documentation]               | API should return correct response when person exists |
|     | ${RESP}                        | send_request    | GET                                 | ${URL}/0
|     | Response code should be equal  | ${RESP}         | 200                                 |
|     | verify_api_response            | ${RESP.json()}  | PEOPLE                              | ${JSON_FILE_SUCCESS_PATH}

| GET /people/{id} non-existing person | 
| ... | [Documentation]                | API should return err msg when person doesn't exist  |
|     | ${RESP}                        | send_request    | GET                                |  ${URL}/1000
|     | Response code should be equal  | ${RESP}         | 404                                |
|     | verify_api_response            | ${RESP.json()}  | ERROR_MSG                          | ${JSON_FILE_NOT_FOUND_PATH}                           


| GET /people/{id} incorrect id       |
| ... | [Documentation]               | API should return err msg when provided id is incorrect |                     |            
|     | ${RESP}                       | send_request                                            | GET                 |  ${URL}/X
|     | Response code should be equal | ${RESP}                                                 | 422                 |          
|     | verify_api_response           | ${RESP.json()}                                          | VALIDATION_ERR_MSG  | ${JSON_FILE_INCORRECT_ID_PATH}

