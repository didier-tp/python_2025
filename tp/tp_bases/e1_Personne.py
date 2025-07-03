class Personne():
    def __init__(self,prenom="?",nom="?",age =0 ):
        self.prenom=prenom
        self.nom=nom
        self.age=age

    def __str__(self):
        return f"Personne prenom={self.prenom} nom={self.nom} age={self.age}"
    
    def decrire(self):
        print(f"Personne prenom={self.prenom} nom={self.nom} age={self.age}")
    
    def incrementer_age(self):
        #self.age = self.age + 1  
        self.age +=1     

