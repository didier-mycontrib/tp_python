se placer dans le répertoire du furtur projet (ex: rest_api_falcon)

virtualenv .venv
---> ça créer un repértoire .venv ressemblant à node_modules de npm (arborescence de packages).

source .venv/bin/activate sous linux
.venv\Scripts\activate.bat sous windows
--> nouveau prompt : (.venv) C:\tp\local-git-repositories\tp_python\rest_api_falcon>

(.venv) C:\...\rest_api_falcon>pip install falcon

create a "virtualenv firrst_module project" with the same name of "real_global_project"
(.venv) ...> mkdir rest_api_falcon
(.venv) ...> touch rest_api_falcon/__init__.py sous linux
(.venv) ...> type nul > rest_api_falcon\__init__.py sous windows
(.venv) ...> touch rest_api_falcon/app.py sous linux
(.venv) ...> type nul > rest_api_falcon\app.py sous windows
etc pour créer l'arborescence suivante de fichiers vides:
rest_api_falcon
     rest_api_falcon
                    __init__.py
		    app.py
		    devise.py
		    devise_api.py

dans rest_api_falcon/rest_api_falcon/devise.py
---------------------------------
class Devise(object) :
	#constructeur avec valeurs par défaut:
	def __init__(self,code=None,name=None,change=0) :
		self.code=code
		self.name=name
		self.change=change
---------------------------------

dans rest_api_falcon/rest_api_falcon/devise_api.py
---------------------------------
import json
import falcon
from .devise import Devise

class DeviseApi(object):

    def on_get(self, req, resp):
        devisesObjects = [ Devise('EUR','Euro',1) , Devise('USD','Dollar',1.1) ]
        devisesDicts = [ vars(e) for e in devisesObjects ]

        # Create a JSON representation of the resource
        resp.body = json.dumps(devisesDicts, ensure_ascii=False)
---------------------------------


dans rest_api_falcon/rest_api_falcon/app.py
---------------------------------
import falcon
from .devise_api import DeviseApi

deviseApi = DeviseApi()

api = application = falcon.API()
api.add_route('/devises', deviseApi); # http://localhost:8000/devises
--------------------------------

Premier lancement (via gunicorn sous linux ou bien via waitress sous windows):

sous linux:
$ source .venv/bin/activate
$ pip install gunicorn
$ gunicorn --reload look.app

sous windows (idealement dans autre terminal/CMD):
.venv\Scripts\activate.bat
(.venv) ...> pip install waitress
(.venv) ...> waitress-serve --port=8000 rest_api_falcon.app:api
Serving on http://DESKTOP-PRO:8000

URL de test: 
http://localhost:8000/devises
Résultat : [{"code": "EUR", "name": "Euro", "change": 1}, {"code": "USD", "name": "Dollar", "change": 1.1}]