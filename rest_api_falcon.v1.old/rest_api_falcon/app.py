import falcon
from rest_api_falcon.devise_api import DeviseApi

deviseApi = DeviseApi()

api = application = falcon.API()
api.add_route('/devises', deviseApi); # http://localhost:8000/devises