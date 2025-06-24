g1=4
var_ambigue=2

def ma_fonction():
    l1=3
    print(f"dans ma_fonction, l1={l1} et g1={g1}")
    # g1=g1+1 ne fonctionne pas ici car python considère ce g1 
    # comme un autre g1 (de niveau local) qui a par hazard le même nom que le g1 global
    '''
    Message d'erreur exact:
       UnboundLocalError: cannot access local variable 'g1' 
       where it is not associated with a value
    '''
    # attention: le comportement de python n'est ici pas le même que celui de javascript
    var_ambigue=12 # cette variable locale là a le même nom que la variable globale
                   #du haut --> 2 cases mémoires distinctes avec même nom , c'est ambigu (pas bien)!!!
    print(f"dans ma_fonction, l1={l1} et g1={g1} et var_ambigue={var_ambigue}")


def ma_fonction2():
    global g1 # le mot clef global permet de déclarer que g1 est ici le nom d'une varaible globale
    l2=3
    print(f"dans ma_fonction2, l2={l2} et g1={g1}")
    g1=g1+1 # g1 est considéré ici (et jusqu'à la fin de cette fonction) comme une variable globale
	# le mot clef global est donc LE MOYEN de modifier si besoin une variable globale primitive
    print(f"dans ma_fonction2,apres incrementation de g1, l2={l2} et g1={g1}")

def ma_fonction3():
    global g2
    g2=3


ma_fonction()
print(f"au niveau principal,après appel à ma_fonction, g1={g1} et var_ambigue={var_ambigue}") 
ma_fonction2()
print(f"au niveau principal,après appel à ma_fonction2, g1={g1}") 
ma_fonction3()
print(f"au niveau principal,après appel à ma_fonction3, g2={g2}") 

##############################

class MySimpleCounter() :

    #constructeur avec valeurs par défaut:
	def __init__(self,val=0) :
		self.val=val
	
	#méthode spéciale __str__ (équivalent à .toString() de java)
	#qui sera automatiquement appelée lors d'un print(cercle):
	def __str__(self) :
		return "MySimpleCounter(val="+str(self.val)+ ")"
		
	def increment(self) :
		self.val+=1
		
	def decrement(self) :
		self.val-=1

#----------

globalCounter1 = MySimpleCounter(1)

def ma_fonction4():
	globalCounter1.increment()
	globalCounter1.increment()
	# ce n'est pas utile d'utiliser le mot clef global car globalCounter1 est une instance d'une classe
	# et on ne fait que modifier une des valeurs internes de l'objet
	print(f"dans ma_fonction4,apres deux appels à increment globalCounter1={globalCounter1}")
	
print(f"au niveau principal,avant appel à ma_fonction4, globalCounter1={globalCounter1}")     
ma_fonction4()
print(f"au niveau principal,après appel à ma_fonction4, globalCounter1={globalCounter1}")  

###############################
# pour cas très pointu seulement, nonlocal permet de déclarer dans une sous fonction imbriquée
# qu'une variable n'est pas locale mais qu'elle est liée à une fonction englobante

def ma_fonction5():
	x=1
	y=2
	print(f"au debut ma_fonction5, x={x}  y={y}")  
	def inner_function():
		x=3
		nonlocal y
		y=3
		print(f"dans ma_fonction5.inner_function, x={x}  y={y}") 
	inner_function() # appel direct de inner_function
	print(f"a la fin de ma_fonction5, x={x}  y={y}") 
	
ma_fonction5()    