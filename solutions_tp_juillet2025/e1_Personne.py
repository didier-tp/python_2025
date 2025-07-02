class Personne():

    #constructeur avec valeurs par défaut:
    def __init__(self,prenom="?",nom="?",age=0):
        self.prenom=prenom
        self.nom=nom
        self.__age=age if age >=0 else 0

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,nouvel_age):
        if nouvel_age>=0:
            self.__age=nouvel_age
        else:
            raise ValueError(f"l'age doit toujours etre positif, {nouvel_age}=valeur invalide")

    def __str__(self):  
        return "Personne(prenom="+str(self.prenom) + ",nom="+str(self.nom) + ",age="+str(self.__age) + ")"  

    def decrire(self):
        print(f"Personne (prenom={self.prenom} nom={self.nom} age={self.age})")

    def incrementer_age(self):   
        self.age +=1

##### Versions initiales (sans @property) , avant exercice 
'''
class Personne():

    #constructeur avec valeurs par défaut:
    def __init__(self,prenom="?",nom="?",age=0):
        self.prenom=prenom
        self.nom=nom
        self.age=age

    def __str__(self):  
        return "Personne(prenom="+str(self.prenom) + ",nom="+str(self.nom) + ",age="+str(self.age) + ")"  

    def decrire(self):
        print(f"Personne (prenom={self.prenom} nom={self.nom} age={self.age})")

    def incrementer_age(self):   
        self.age +=1
'''