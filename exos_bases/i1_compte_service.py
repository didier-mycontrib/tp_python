from e3_Compte import Compte

# en local dans singleton.py
from i1_singleton import Singleton

#version 2 , couplée avec l'accès à la base de données sqlite via h1_CompteDao , h1_db_params.py

from h1_CompteDao import CompteDao
from h1_db_params import my_db_name, my_db_url , my_db_sql_alchemy_engine

class CompteService(metaclass=Singleton):
    def __init__(self):
        self.compte_dao = CompteDao(my_db_sql_alchemy_engine)

    def getComptes(self):
        listeComptes = self.compte_dao.allComptes()
        print(">>> CompteService.listeComptes=", listeComptes)
        return listeComptes

    def getCompteById(self , id ):
        c=self.compte_dao.compteByNum(int(id))
        print(f">>> CompteService.getCompteById , id={id} , c={c}")
        return c

    def createCompte(self , c: Compte):
        print(f">>> CompteService.createCompte , c={c}")
        return self.compte_dao.insertNewCompte(c)
       
    def updateCompte(self, c: Compte):
        print(f">>> CompteService.updateCompte , c={c}")
        self.compte_dao.updateCompte(c)

    def deleteCompteById(self, id):
        print(f">>> CompteService.deleteCompteById , id={id} ")
        self.compte_dao.deleteCompteByNum(int(id))
        #temporairement (on peut mieux faire pour adapter):
        return Compte(int(id),"compte supprimé",0.0)
    
'''   
#version 1 simulee sans base de données , simple map/dictionnary en memoire

class CompteService(metaclass=Singleton):
    def __init__(self):
        self.ComptesDict = {}
        self.ComptesDict[1] = Compte(1 , 'compte_a', 50.0)
        self.ComptesDict[2] = Compte(2 , 'compte_b', 60.0)
        self.ComptesDict[3] = Compte(3 , 'compte_c', 70.0)
        self.ComptesDict[4] = Compte(4 , 'compte_d', 80.0)

    def getComptes(self):
        listeComptes = list(self.ComptesDict.values())
        print(">>> listeComptes=", listeComptes)
        return listeComptes

    def getCompteById(self , id ):
        return self.ComptesDict.get(int(id))

    def createCompte(self , c: Compte):
        if c.numero :
           key = int(c.numero)
        else:
           key = c.numero = Compte.auto_incr_num()
        if key in self.ComptesDict:
            raise Exception("conflict : an existing Compte have same numero:"+key )
        else:
            self.saveCompte(c)

    def updateCompte(self, c: Compte):
        key = int(c.numero)
        if key in self.ComptesDict:
            self.saveCompte(c)
        else:
            raise Exception("cannot update : no Compte found for numero:"+ key)

    def saveCompte(self , c : Compte ):
        self.ComptesDict[int(c.numero)]=c

    def deleteCompteById(self, id):
        return self.ComptesDict.pop(int(id),None)    

'''        