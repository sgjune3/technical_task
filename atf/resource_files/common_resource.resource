|  *** Settings ***  |
|  Documentation     |  A common resource file containing shared variables and libraries imports
|  Library           |  ../libraries/ApiLibrary.py

|  *** Variables *** |
|  ${HOST}           |  http://127.0.0.1:8000
|  ${BASE_URL}       |  ${HOST}/api

| *** Keywords ***               |                             |                            |
| Response code should be equal  | [Arguments]                 | ${response}                | ${expected_response_code}
|                                | Should Be Equal As Integers | ${response.status_code}    | ${expected_response_code}