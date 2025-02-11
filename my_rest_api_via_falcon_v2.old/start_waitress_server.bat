cd /d %~dp0
pipenv run waitress-serve --port=8000 my_rest_api.app:api
