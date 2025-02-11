from devise import Devise

from singleton import Singleton

#version simulee sans base de données , simple map/dictionnary en memoire

class DeviseService(metaclass=Singleton):
    def __init__(self):
        self.devisesDict = {};
        self.devisesDict["EUR"] = Devise('EUR', 'Euro', 1)
        self.devisesDict["USD"] = Devise('USD', 'Dollar', 1.1)
        self.devisesDict["JPY"] = Devise('JPY', 'Yen', 130)
        self.devisesDict["GPB"] = Devise('GBP', 'Livre', 0.9)

    def getDevises(self):
        return self.devisesDict;

    def getDeviseById(self , id ):
        return self.devisesDict.get(id);

    def saveDevise(self , dev : Devise ):
        self.devisesDict[dev.code]=dev;

    def deleteDeviseById(self, id):
        self.devisesDict.pop(id,None);