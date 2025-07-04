class Compte():
    def __init__(self,numero=0,label="compte_courant", solde=0.0):
        self.numero=numero
        self.label=label
        self.solde=solde

    def __str__(self):
        return f"Compte numero={self.numero} label={self.label} solde={self.solde}"

    def debiter(self,montant):
        self.solde = self.solde -montant

    def crediter(self,montant):
        self.solde = self.solde +montant    

    def __gt__(self,other):
        return (self.solde > other.solde)    