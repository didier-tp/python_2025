##### avec attributs/variable de classe

class CompteEpargne :
    tauxInteret = 1.25 # valeur par defaut liee à l'ensemble de la classe
                       # variable de classe (pas liée à self)
    def __init__(self,num,label,solde):
        self.num=num
        self.label=label
        self.solde=solde
    
    def __str__(self):
        return f'CompteEpagne num={self.num} label={self.label} solde={self.solde} avec tauxInteret = {CompteEpargne.tauxInteret}'


ce1 = CompteEpargne(1,"compteEpargne1",50.0)
ce2 = CompteEpargne(2,"compteEpargne2",100.0)
print("ce1,",ce1); print("ce2,",ce2)
CompteEpargne.tauxInteret=2.1 
print("ce1,",ce1); print("ce2,",ce2)

#### méthodes statiques ( @staticmethod )

class MyBasicUtils:
    @staticmethod
    def addition(a, b):
        return a + b

# Appel direct sans créer d'instance
print("MyBasicUtils.addition(3, 5)=",MyBasicUtils.addition(3, 5))  # Sortie : 8

################ avec méthode de classe (@classmethod)

class CompteAvecTauxInteret:
    tauxInteret = 1.25 #partagé au niveau classe , avec valeur par défaut

    def __init__(self,name):
        self.name=name

    def __str__(self):
        return f'CompteAvecTauxInteret name={self.name} avec tauxInteret={CompteAvecTauxInteret.tauxInteret}' 

    @classmethod # pour utilisation de cls. à la place de .self 
    def augmenterTauxInteret(cls,augmentation):
        # cls. permet d'accéder à la classe courante (iciCompteAvecTauxInteret)
        cls.tauxInteret += augmentation

# Utilisation de la méthode de classe
c1 = CompteAvecTauxInteret("c1")
c2 = CompteAvecTauxInteret("c2")
print(c1);print(c2)
CompteAvecTauxInteret.augmenterTauxInteret(0.5) # + 0.5% 
print(c1);print(c2)

########### propriétés (avec @property et  setter)


class Personne :

    def __init__(self,nom,taille):
        self.nom=nom
        self.__taille=taille if taille >=0 else 0
        
    def __str__(self):
        return f'Personne nom={self.nom} taille={self.__taille}'        

    @property
    def taille(self):
        return self.__taille
    
    @taille.setter
    def taille(self, nouvelle_taille):
        if nouvelle_taille < 0:
            raise ValueError(f"la taille ne peut pas etre négative; nouvelle_taille={nouvelle_taille} invalide")
        else:
            self.__taille = nouvelle_taille

p = Personne("toto",170)
print(p, "p.taille=", p.taille)
try:
    p.taille = p.taille - 220
except ValueError as e:
    print(e)
print(p)
p.taille = 180
print(p)


##########  HERITAGE MULTIPLE #######

class Avion:
    def __init__(self,altitude=0):
        self.altitude=altitude

    def voler(self):
        print("volant à l'altitude="+str(self.altitude))


class Flottant:
    def __init__(self,nbFlotteurs=2):
        self.nbFlotteurs=nbFlotteurs

    def pouvantFlotter(self) :  
        print("pouvant flotter avec nbFlotteurs="+str(self.nbFlotteurs))   

class Hydravion(Avion,Flottant):
    def __init__(self,nbFlotteurs=2):
        Avion.__init__(self,0); #altitude initiale=0
        Flottant.__init__(self,nbFlotteurs)

h1 = Hydravion()
h1.altitude=1250
h1.voler()
h1.pouvantFlotter()
