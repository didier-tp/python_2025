from devise import Devise

# en local dans singleton.py
from singleton import Singleton

#version simulee sans base de données , simple map/dictionnary en memoire

class DeviseService(metaclass=Singleton):
    def __init__(self):
        self.devisesDict = {};
        self.devisesDict["EUR"] = Devise('EUR', 'Euro', 1)
        self.devisesDict["USD"] = Devise('USD', 'Dollar', 1.1)
        self.devisesDict["JPY"] = Devise('JPY', 'Yen', 130)
        self.devisesDict["GBP"] = Devise('GBP', 'Livre', 0.9)

    def getDevises(self):
        listeDevises = list(self.devisesDict.values());
        print(">>> listeDevises=", listeDevises);
        return listeDevises;

    def getDeviseById(self , id ):
        return self.devisesDict.get(id);

    def createDevise(self , dev: Devise):
        key = dev.code;
        if key in self.devisesDict:
            raise Exception("conflict : an existing Devise have same key/code:"+key );
        else:
            self.saveDevise(dev);

    def updateDevise(self, dev: Devise):
        key = dev.code;
        if key in self.devisesDict:
            self.saveDevise(dev);
        else:
            raise Exception("cannot update : no Devise found for key/code:"+ key);

    def saveDevise(self , dev : Devise ):
        self.devisesDict[dev.code]=dev;

    def deleteDeviseById(self, id):
        return self.devisesDict.pop(id,None);