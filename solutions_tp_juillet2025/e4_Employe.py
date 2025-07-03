#### classe Employe heritant de Personne en python
from e1_Personne import Personne

class Employe(Personne):

    #constructeur avec valeurs par défaut:
    def __init__(self,prenom="?",nom="?",age=0,fonction="?",salaire=0):
        #Personne.__init__(self,prenom,nom,age) # python 2 ou 3
        super().__init__(prenom,nom,age) # python 3
        self.fonction=fonction
        self.salaire=salaire
	
    def __str__(self):
        return f"Employe (prenom={self.prenom} ,nom={self.nom} ,age={self.age} ,fonction={self.fonction} ,salaire={self.salaire})"
		
    def decrire(self):
        super().decrire()
        print(f"\tde type Employe avec fonction={self.fonction} et salaire={self.salaire}")

   