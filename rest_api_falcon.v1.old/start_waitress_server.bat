cd /d %~dp0
call .venv\Scripts\activate.bat 
waitress-serve --port=8000 rest_api_falcon.app:api
