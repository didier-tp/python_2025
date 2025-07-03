from abc import ABC, abstractmethod
#NB: ABC signifie AbstractBaseClass

########## Classe abstraite Porte

class Porte(ABC):

    #constructeur avec valeurs par défaut:
    def __init__(self,nom="",fermee=True):
        self.nom=nom
        self.fermee=fermee

    def etat(self):
        return "fermee" if self.fermee else "ouverte"

    def __str__(self):
        return f"Porte de type={self.type_porte()} de nom={self.nom} qui est {self.etat()}"
		
    def decrire(self):
         print(self.__str__() )

    @abstractmethod
    def ouvrir(self):
        pass

    @abstractmethod
    def type_porte(self):
        pass

    @abstractmethod
    def fermer(self):
        pass

########### classe concrete PortePivotante héritant de Porte

class PortePivotante(Porte):

    def __init__(self,nom="",fermee=True):
         super().__init__(nom,fermee)

    def type_porte(self):
        return "pivotante"    

    def ouvrir(self):
        print(f"angle ouverture=90 ° pour porte {self.nom}")
        self.fermee=False

    def fermer(self):
        print(f"angle ouverture=0 ° pour porte {self.nom}")
        self.fermee=True         

########### classe concrete PorteCoulissante héritant de Porte

class PorteCoulissante(Porte):

    def __init__(self,nom="",fermee=True):
         super().__init__(nom,fermee)

    def type_porte(self):
        return "coulissante"    

    def ouvrir(self):
        print(f"ouverture sur glissière=80 cm pour porte {self.nom}")
        self.fermee=False

    def fermer(self):
        print(f"ouverture sur glissière=0 cm pour porte {self.nom}")
        self.fermee=True         
                