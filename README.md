# Setup
1. install Python (tested on Python 3.10.X)
2. clone repository
3. `cd` to the cloned repo folder
4. create venv `python -m venv venv` or `python3 -m venv venv`
5. activate venv 
   1. On Windows run `.\venv\Scripts\activate`
   2. On Linux `source venv/bin/activate`
6. install required dependencies `pip install -r requirements.txt`

# Usage

##### Prerequisites
`cd` to the cloned repo folder

### Unit tests
* to execute all unit tests run `python -m pytest .`
* to execute only ATF unit tests run `python -m pytest atf`
* to execute only REST API unit tests run `python -m pytest rest_api`

## REST API

### Starting uvicorn server
* to start uvicorn server run `uvicorn rest_api.main:app --log-config ./rest_api/log.ini`. To use a different port/host please use `--host <str>` and/or `--port <int>`. For more configuration options check the official uvicorn page: https://www.uvicorn.org/settings/

### Swagger
* after starting uvicorn server swagger is exposed on `<host>:<port>/docs`
* all information about endpoints, allowed methods, status codes, etc. can be found here

### Endpoints
* GET /api/people/{person_id}
* GET /api/planets/{planet_id}
* GET /api/starships/{starship_id}
* check swagger for detailed documentation, examples etc.

### Logs
* Logs are stored by default in the `log_file.log` file.

## ATF (Automation Testing Framework)

### RobotFramework
* ATF contains two types of API tests: _**performance**_ and _**functional**_ 
* tests are stored in `atf/robot_files` folder
* to execute functional tests run `python -m robot -i functional atf/robot_files/` or `python -m robot -i task_1 atf/robot_files/`
* to execute performance tests run `python -m robot -i performance atf/robot_files/` or `python -m robot -i task_2 atf/robot_files/`
* test results by default are stored in log.html, report.html, and output.xml files
* at the begging of each test suit API is started, and after execution closed. To configure the host, port, etc. use the config file located in `atf/configs/config.py`