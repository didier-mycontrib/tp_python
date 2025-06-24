
from flask  import Flask , jsonify , abort , request
app = Flask(__name__)

from e3_Compte import Compte
from i1_compte_service import CompteService

api_prefix="/minibank-api/v1/comptes" #default sever url in dev mode: http://localhost:5000

#NB: by default flask and fastapi produces JSONResponse so dictionnary or list of dictionary are automatically
# transform as json string , no need of json.dumps(...., ensure_ascii=False) or falsk.jsonify()

# util function for convertir data object to dictionary 
def asJsonSerializableDict(objOrCol):
    #print("type=",type(objOrCol))
    if isinstance(objOrCol,(list,tuple)):
        return [ obj.__dict__ for obj in objOrCol ]
    else: 
        return objOrCol.__dict__
    
def asDict(objOrCol): # shorter function name for frequent calls
    return asJsonSerializableDict(objOrCol) 

@app.get(f"{api_prefix}/<id>" ) #NB method param id should have same name that PathVariable <id>
def get_Compte_by_id(id):
    try:
        print("(get_Compte_by_id() call with id=" , id)
        return asDict(CompteService().getCompteById(id))
    except Exception as e:
        abort(404,f"Compte not found for id={id}")


@app.post(f"{api_prefix}" )
def create_Compte():
    try :
        data = request.get_json() # (as dict if possible) from POST request body
        #print("jsonData received(as disct) in post mode",data)
        c=Compte(label=data['label'],solde=data['solde'])
        #print("Compte received in post mode",c)
        CompteService().createCompte(c)
        #return asDict(c) # with default status code = 200/OK
        return asDict(c) , 201 # with specific status code = 201/CREATED
    except Exception as e:
        abort(409,str(e))


@app.put(f"{api_prefix}/<id>" )
def update_Compte(id):
    try:
        data = request.get_json() # (as dict if possible) from PUT request body
        #print("jsonData received(as disct) in put mode",data)
        c=Compte(data['numero'],data['label'],data['solde'])
        #print("Compte received in put mode",c)
        c.numero =id
        CompteService().updateCompte(c)
        return asDict(c) # with default status code = 200/OK
    except Exception as e:
         abort(404,str(e))


@app.delete(f"{api_prefix}/<id>" ) 
def delete_Compte(id):
    deletedCompte = CompteService().deleteCompteById(id)
    if deletedCompte==None :
        abort(404,f"no Compte (to Delete) found for numero=={id}")
    else:
        #return "Compte was sucessfully deleted" # with default status code = 200/OK
        return '', 204 # with specific status code = 204/NO_CONTENT


@app.get(f"{api_prefix}/" )
def get_Comptes():
    return asDict(CompteService().getComptes()) #will be automatically JSON serializd by jsonify() of flask

    #default flask behavior : 
    # if return resAsDict or resAsCollectionOfDict 
    # automatic return  jsonify(resAsDict)

