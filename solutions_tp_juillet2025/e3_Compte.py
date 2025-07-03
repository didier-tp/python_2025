class Compte():

    last_max_num_compte=0; #partagé au niveau classe , avec valeur par 
                       #pour simuler auto incrementation

    @classmethod # pour utilisation de cls. à la place de .self 
    def auto_incr_num(cls):
        # cls. permet d'accéder à la classe courante (ici Compte)
        cls.last_max_num_compte += 1
        return cls.last_max_num_compte                      

    #constructeur avec valeurs par défaut:
    def __init__(self,numero=0,label="?",solde=0.0):
        self.numero=numero
        self.label=label
        self.solde=solde
        Compte.last_max_num_compte=max(self.numero,Compte.last_max_num_compte)

    def __str__(self):  
        return f"Compte(numero={self.numero} ,label={self.label}, solde={self.solde} ) "  

    def debiter(self, montant):   
        self.solde -= montant

    def crediter(self, montant):   
        self.solde += montant

    #pour surcharge de l'operateur > (exercice f5)
    def __gt__(self, other):
        return (self.solde > other.solde)


########## version 1 (sans attribut partagé au niveau de la classe et sans @classmethode)

'''
class Compte():

    #constructeur avec valeurs par défaut:
    def __init__(self,numero=0,label="?",solde=0.0):
        self.numero=numero
        self.label=label
        self.solde=solde

    def __str__(self):  
        return f"Compte(numero={self.numero} ,label={self.label} solde={self.solde} ) "  

    def debiter(self, montant):   
        self.solde -= montant

    def crediter(self, montant):   
        self.solde += montant
'''