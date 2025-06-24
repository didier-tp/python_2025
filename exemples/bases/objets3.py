from abc import ABC, abstractmethod

########### code de la classe AnimalDomestique en python :
#NB: ABC signifie AbstractBaseClass
class AnimalDomestique(ABC):

    #constructeur avec valeurs par défaut:
    def __init__(self,nom=""):
        self.nom=nom
	
	#méthode spéciale __str__ (équivalent à .toString() de java)
	#qui sera automatiquement appelée lors d'un print(animal):
    def __str__(self):
        return f"AnimalDomestique(nom={self.nom})"
		
    def decrire(self):
         print("AnimalDomestique de nom=",self.nom)

    @abstractmethod
    def parler(self):
        pass

#### classe Chat héritant de AnimalDomestique:

class Chat(AnimalDomestique):

    #constructeur avec valeurs par défaut:
    def __init__(self,nom="ChatChat",nbHeuresSommeil=14):
        #AnimalDomestique.__init__(self,nom)
        super().__init__(nom)
        self.nbHeuresSommeil=nbHeuresSommeil
	
	#méthode spéciale __str__ (équivalent à .toString() de java)
	#qui sera automatiquement appelée lors d'un print(chat):
    def __str__(self):
        return f"Chat(nom={self.nom} ,nbHeuresSommeil={self.nbHeuresSommeil} )"

    def decrire(self):
        print("Je suis un chat qui dort ",self.nbHeuresSommeil, " h")
        super().decrire()
        #AnimalDomestique.decrire(self)
    	
    def parler(self):
        print("miaou miaou")
        
    def ronronner(self):
        print("ronron ...")        
     
#### classe Chien héritant de AnimalDomestique:

class Chien(AnimalDomestique):

    #constructeur avec valeurs par défaut:
    def __init__(self,nom="ChienChien",fonction="?"):
        #AnimalDomestique.__init__(self,nom)
        super().__init__(nom)
        self.fonction=fonction
	
	#méthode spéciale __str__ (équivalent à .toString() de java)
	#qui sera automatiquement appelée lors d'un print(chat):
    def __str__(self):
        return f"chien(nom={self.nom} ,fonction={self.fonction} )"

    def decrire(self):
        print("Je suis un chien , fonction= ",self.fonction)
        super().decrire()
        #AnimalDomestique.decrire(self)
		
    def parler(self):
        print("whaouf whaouf")
        
    def monterLaGarde(self):
        print("je monte la garde ...")        
      
     
###### utilisation de la classe AnimalDomestique 
###### et de ses sous classes		
		
		
'''
#partie impossible si la classe AnimalDomestique est abstraite
a=AnimalDomestique() #impossible d'instancier une classe abstraite
a.nom="animal_domestique_inconnu"
a.decrire()
a.parler()
'''

chat1 = Chat( "malo" , 15)
print(chat1)
chat1.decrire()
chat1.parler()
chat1.ronronner()
print("chat1_as_dict:" , vars(chat1))

chien1 = Chien( "medor" , "gardien de troupeau" )
print(chien1)
chien1.decrire()
chien1.parler()
chien1.monterLaGarde()
print("chien1_as_dict:" , vars(chien1))

#polymorphisme en boucle :
listeAnimaux = []
listeAnimaux.append(chat1)
listeAnimaux.append(chien1)
for a in listeAnimaux:
    print("\n pour a de type=", type(a))
    a.decrire()
    a.parler()
    '''
    #mais surtout pas :
    if isinstance(a,Chat):
        a.decrire_chat();
        a.miauler()
    else:
        a.decrire_chien();
        a.aboyer()
    '''
    
print("\n")
print("isinstance(chat1,Chat):" ,  isinstance(chat1,Chat))
print("issubclass(Chat,AnimalDomestique):" ,  issubclass(Chat,AnimalDomestique))


'''
# anciennes versions des constructeurs hérités:

class Chat(AnimalDomestique):

    #constructeur avec valeurs par défaut:
    def __init__(self,nbHeuresSommeil=14,*args, **kwargs):
        #AnimalDomestique.__init__(self,*args, **kwargs)
        super().__init__(*args, **kwargs)
        self.nbHeuresSommeil=nbHeuresSommeil


# défaut : paramètres secondaires/additionnels pas en dernière position
# car *args, **kwargs uniquement possible en dernière position

chat1 = Chat( 15 , "malo")

'''