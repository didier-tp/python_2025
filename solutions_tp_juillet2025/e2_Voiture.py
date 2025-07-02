
class Voiture():

    #constructeur avec valeurs par défaut:
    def __init__(self,marque="?",modele="?",couleur="white",vitesse=0):
        self.marque=marque
        self.modele=modele
        self.couleur=couleur
        self.vitesse=vitesse

    def __str__(self):  
        return f"Voiture(marque={self.marque} ,modele={self.modele} couleur={self.couleur} vitesse={self.vitesse}) "  

    def accelerer(self, delta=1):   
        self.vitesse += delta

    def ralentir(self, delta=1):   
        self.vitesse -= delta
        if self.vitesse < 0 :
            self.vitesse=0
