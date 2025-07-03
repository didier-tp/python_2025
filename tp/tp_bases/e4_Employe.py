from e1_Personne import Personne

class Employe(Personne):
    def __init__(self,prenom="?",nom="?",age =0,salaire=0,fonction="?"):
        super().__init__(prenom,nom,age) # déclenche indirectement self.prenom=prenom, etc
        self.salaire=salaire
        self.fonction=fonction

    def __str__(self):
        return f"Employe salaire={self.salaire} fonction={self.fonction} heritant de " +  super().__str__()