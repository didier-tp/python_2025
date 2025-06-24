#p4.py : fonctions

#fonction basique sans paramètre retournant une valeur fixe:
def generer_message_salutation():
	message="bonjour"
	return message
	
#fonction/procedure basique ne retournant aucune valeur
#mais exécutant une action:	
def saluer():
	salutation=generer_message_salutation() #appel de sous-fonction
	print(salutation)	
	
saluer() #l'appel de la fonction déclenche l'affichage de bonjour

#fonction multiplier avec 2 parametres formels a et b
def multiplier(a,b):
	return a*b
	
x=4; y=5;
res = multiplier(x,y); # appel de la fonction multiplier en passant
                       # les valeurs des paramètres effectifs x et y
					   # lors de l'appel a est une copie de x
					   # et b est une copie de y

print("res=",res) # affiche res=20


########### lambda

def carre(x):
	return x*x

print("carre(4)=", carre(4)) #16

lambda_carre = lambda x : x*x
print("type(lambda_carre)=", type(lambda_carre)) #<class 'function'>
print("lambda_carre(4)=", lambda_carre(4)) #16

lambda_mult = lambda x,y : x*y
print("lambda_mult(2,3)=", lambda_mult(2,3)) #6

import datetime;
lambda_return_now = lambda  maintenant=datetime.datetime.now() :maintenant.time()
print("heure=" , lambda_return_now()) # 18:16:54.789809

def enchainer_calcul_et_affichage_avec_prefixage(x, f_calcul ,f_prefixage):
	res = f_calcul(x)
	print(f_prefixage(res))

enchainer_calcul_et_affichage_avec_prefixage(6 , 
		lambda x:x*x ,lambda expr : '** ' + str(expr))	# ** 36	

enchainer_calcul_et_affichage_avec_prefixage(6 , 
		lambda x:x+x ,lambda expr : '>> ' + str(expr)) # >> 12	


############## paramétres optionnels et nommés

def display_val(val , color="blue" ,comment ="no comment"):
	message=str(val)+ " color="+color + " comment="+comment
	print(message)

display_val(5,"red","with_all_params")
#5 color=red comment=with_all_params

display_val(8,"green")#with default comment	
#8 color=green comment=no comment

display_val(7) # with default color and comment
#7 color=blue comment=no comment

display_val(comment="with_named_params",val=9)	#with named params
#9 color=blue comment=with_named_params


####### fonction à nombre d'arguments variables (*args, **kwargs)
# **kwargs for keyword args or **kvargs for keyValue args

def display_args(*args):
	for a in args:
		print("a=",a)

def display_keyword_args(**kvargs):
	for k,v in kvargs.items():
		print("k=",k,"v=",v)

def display_args_and_keyword_args(*args,**kwargs):
	for a in args:
		print("a=",a)
	for k,v in kwargs.items():
		print("k=",k,"v=",v)				


def somme_args(*args):
	s=0
	for a in args:
		s+=a
	return s

def somme_any_args(*args,**kwargs):
	s=0
	for a in args:
		s+=a
	for v in kwargs.values():
		s+=v
	return s

display_args(2,6,8) # a= 2 , a= 6 , a= 8
print("sommeArgs=",somme_args(2,6,8)) # 16

display_keyword_args(a=1,b=3,c=5)#k= a v= 1 , k= b v= 3 , k= c v= 5
display_args_and_keyword_args(2,6,8,a=1,b=3,c=5) #ok
#display_args_and_keyword_args(a=1,b=3,c=5,2,6,8) #error , positional args should be first

print("sommeAnyArgs=",somme_any_args(2,6,8,a=1,b=3,c=5)) # 25