import json
import falcon
from rest_api_falcon.devise import Devise

class DeviseApi(object):

    def on_get(self, req, resp):
        devisesObjects = [ Devise('EUR','Euro',1) , Devise('USD','Dollar',1.1) ];
        devisesDicts = [ vars(e) for e in devisesObjects ]

        # Create a JSON representation of the resource
        resp.body = json.dumps(devisesDicts, ensure_ascii=False)
        '''
        # The following line can be omitted because 200 is the default
        # status returned by the framework, but it is included here to
        # illustrate how this may be overridden as needed.
        resp.status = falcon.HTTP_200
		'''