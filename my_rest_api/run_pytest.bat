cd /d %~dp0
REM pipenv run pytest --version
REM pipenv run pytest --help
pipenv run pytest my_pytests
REM NB1: pystest run all tests with name like xxx_test.py or test_xx.py
REM NB2: my_pytests directory name is essential for pytest command to properly interpret import in xx_test.py files
pause