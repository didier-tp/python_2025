

########### code de la classe Figure en python :

class Figure:

    #constructeur avec valeurs par défaut:
    def __init__(self,x=0,y=0,color="black"):
        self.x=x
        self.y=y
        self.color=color
	
	#méthode spéciale __str__ (équivalent à .toString() de java)
	#qui sera automatiquement appelée lors d'un print(cercle):
    def __str__(self):
        return f"Figure(x={self.x} ,y={self.y} ,color={self.color})"
		
    def perimetre(self):
        return 0
		
    def aire(self):
        return 0
        
    def deplacer(self,dx,dy):
        self.x=self.x+dx
        self.y=self.y+dy
        
    def afficher(self):
        print(f"Figure(x={self.x} ,y={self.y} ,color={self.color})")

########### code de la classe Cercle héritant de Figure :
import math
class Cercle(Figure):

    #constructeur avec valeurs par défaut:
    def __init__(self,xc=0,yc=0,rayon=0,color="black"):
        #self.x=xc;self.y=yc;self.color=color #not advised
        #Figure.__init__(self,xc,yc,color) #ok python 2 et 3
        super().__init__(xc,yc,color) #ok python 3
        self.rayon=rayon
	
	#méthode spéciale __str__ (équivalent à .toString() de java)
	#qui sera automatiquement appelée lors d'un print(cercle):
    def __str__(self):
        return f"Cercle xc={self.x} ,yc={self.y} ,rayon={self.rayon} ,color={self.color})"
		
    def perimetre(self):
        return 2*math.pi*self.rayon
		
    def aire(self):
        return math.pi*self.rayon*self.rayon
    
    def afficher(self):
        print(f"Cercle(rayon={self.rayon})", end =" heritant de ")
        super().afficher()
                

########### code de la classe Rectangle héritant de Figure :

class Rectangle(Figure):

    #constructeur avec valeurs par défaut:
    def __init__(self,x=0,y=0,largeur=0,hauteur=0,color="black"):
        #self.x=x; self.y=y; self.color=color #not advised
        #Figure.__init__(self,x,y,color) # python 2 ou 3
        super().__init__(x,y,color) # python 3
        self.largeur=largeur
        self.hauteur=hauteur
	
	#méthode spéciale __str__ (équivalent à .toString() de java)
	#qui sera automatiquement appelée lors d'un print(rectangle):
    def __str__(self):
        return f"Rectangle (x={self.x} ,y={self.y} ,largeur={self.largeur} ,hauteur={self.hauteur} ,color={self.color} )"
		
    def perimetre(self):
        return 2*(self.largeur + self.hauteur)
		
    def aire(self):
        return self.largeur*self.hauteur
              
    def afficher(self):
        print(f"Rectangle(largeur={self.largeur} ,hauteur={self.hauteur})" , end =" heritant de ")
        super().afficher()

     
        
###### utilisation des classes Figure , Cercle et Rectangle		
		
f1=Figure()
f2=Figure(50,50,"red"); f2.deplacer(10,10)
print("f1=",f1)  
print("f2=",f2)
f2.afficher()        
		
c1=Cercle() #instanciation (pas de mot clef new) mais nom de classeq
             #vue comme fonction créant une nouvelle instance
c1.rayon=40
print("c1=",c1)  
print("rayon de c1=",c1.rayon) # rayon de c1= 40
print("perimetre de c1=",c1.perimetre()) # perimetre de c1= 251.32741228718345
print("surface de c1=",c1.aire()) # surface de c1= 5026.548245743669

c2=Cercle(40,60,20) # Cercle(xc,yc,rayon)
print("rayon de c2=",c2.rayon) # rayon de c2= 20

print("c2=" , c2) # équivalent à print("c2=" , str(c2)) 
c2.afficher()
# affiche c2= Cercle(xc=40,yc=60,rayon=20)

c2.deplacer(10,30)
print("apres c2.deplacer(10,30) c2=" , c2)
print("c2=",c2) 

print("type(c2)=",type(c2)) # <class '__main__.Cercle'>
#c2AsDict = c2.__dict__ # ok mais moins bien que vars(...)
c2AsDict = vars(c2) # converti un objet en un dictionnaire
print("c2AsDict=",c2AsDict) # {'xc': 40, 'yc': 60, 'rayon': 20}
print("type(c2AsDict)=",type(c2AsDict)) #  <class 'dict'>

r1=Rectangle(15,15,200,150)
print("largeur de r1=",r1.largeur)
print("r1=",r1)
r1.deplacer(10,30)
print("apres r1.deplacer(10,30) r1=" , r1)
r1.afficher()
print("perimetre de r1=",r1.perimetre())
print("surface de r1=",r1.aire()) 

print("issubclass(Cercle,Figure):" ,  issubclass(Cercle,Figure))
print("issubclass(Cercle,Rectangle):" ,  issubclass(Cercle,Rectangle))

#polymorphisme en boucle :
listeFigures = []
listeFigures.append(c1)
listeFigures.append(Cercle(100,150,50,"red"))
listeFigures.append(r1)
listeFigures.append(Rectangle(200,200,60,70,"orange"))
for f in listeFigures:
    f.deplacer(3,2)
    print("\nPour f de type=", type(f))
    f.afficher()
    print("isinstance(f,Cercle):" ,  isinstance(f,Cercle))
    print("isinstance(f,Rectangle):" ,  isinstance(f,Rectangle))
    print("isinstance(f,Figure):" ,  isinstance(f,Figure))
    print("------------------------------")

