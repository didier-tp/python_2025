import math

########### code de la classe Cercle en python :

class Cercle():

    #constructeur avec valeurs par défaut:
    def __init__(self,xc=0,yc=0,rayon=0):
        self.xc=xc
        self.yc=yc
        self.rayon=rayon
	
	#méthode spéciale __str__ (équivalent à .toString() de java)
	#qui sera automatiquement appelée lors d'un print(cercle):
    def __str__(self):
        return "Cercle(xc="+str(self.xc) + ",yc="+str(self.yc) + ",rayon="+str(self.rayon) + ")"
		
    def perimetre(self):
        return 2*math.pi*self.rayon
		
    def aire(self):
        return math.pi*self.rayon*self.rayon
        
    def deplacer(self,dx,dy):
        self.xc=self.xc+dx
        self.yc=self.yc+dy         

########### code de la classe Rectangle en python :

class Rectangle():

    #constructeur avec valeurs par défaut:
    def __init__(self,x=0,y=0,largeur=0,hauteur=0):
        self.x=x
        self.y=y
        self.largeur=largeur
        self.hauteur=hauteur
	
	#méthode spéciale __str__ (équivalent à .toString() de java)
	#qui sera automatiquement appelée lors d'un print(rectangle):
    def __str__(self):
        return "Rectangle(x="+str(self.x) + ",y="+str(self.y) + ",largeur="+str(self.largeur) + ",hauteur="+str(self.hauteur) + ")"
		
    def perimetre(self):
        return 2*(self.largeur + self.hauteur)
		
    def aire(self):
        return self.largeur*self.hauteur
        
    def deplacer(self,dx,dy):
        self.x=self.x+dx
        self.y=self.y+dy         


#### Compte en python:
# ._attribut_protected , .__attribut_prive
class Compte:
    decouvertAutorise=-200.0;
    def __init__(self,numero=0,solde=0):
        self.__numero=numero
        self.__solde=solde
        
### utilisation de compte

c1 = Compte(1,250.0)
c1.__newAttribute="newValue";
#print("c1.__solde=" , c1.__solde) #interdit car .__solde est privé
print("c1 as dict =" , vars(c1)) 
print("Compte.decouvertAutorise=" , Compte.decouvertAutorise) 
Compte.decouvertAutorise=-300.0
print("Compte.decouvertAutorise=" , Compte.decouvertAutorise)       
        
###### utilisation de la classe Cercle		
		
		
c1=Cercle(); #instanciation (pas de mot clef new) mais nom de classe
             #vue comme fonction créant une nouvelle instance
c1.rayon=40;
print("rayon de c1=",c1.rayon) # rayon de c1= 40
print("perimetre de c1=",c1.perimetre()) # perimetre de c1= 251.32741228718345
print("surface de c1=",c1.aire()) # surface de c1= 5026.548245743669

c2=Cercle(40,60,20) # Cercle(xc,yc,rayon)
print("rayon de c2=",c2.rayon) # rayon de c2= 20

print("c2=" , c2) # équivalent à print("c2=" , str(c2)) 
# affiche c2= Cercle(xc=40,yc=60,rayon=20)

c2.deplacer(10,30)
print("apres c2.deplacer(10,30) c2=" , c2)

print("type(c2)=",type(c2)) # <class '__main__.Cercle'>
#c2AsDict = c2.__dict__ # ok mais moins bien que vars(...)
c2AsDict = vars(c2) # converti un objet en un dictionnaire
print("c2AsDict=",c2AsDict) # {'xc': 40, 'yc': 60, 'rayon': 20}
print("type(c2AsDict)=",type(c2AsDict)) #  <class 'dict'>

r1=Rectangle(15,15,200,150);
print("largeur de r1=",r1.largeur);
print("r1=",r1);
r1.deplacer(10,30)
print("apres r1.deplacer(10,30) r1=" , r1)
print("perimetre de r1=",r1.perimetre())
print("surface de r1=",r1.aire()) 