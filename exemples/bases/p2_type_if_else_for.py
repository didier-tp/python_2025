a=15
print(type(a)) #affiche int ou <class 'int'>

s="abc"
print(type(s)) #affiche str ou <class 'str'>

x=2.4
print(type(x)) #affiche float ou <class 'float'>

c1=2+3j
print(type(c1)) #affiche complex ou <class 'complex'>

l1=['rouge' , 'vert' , 'bleu' ]
print(type(l1)) #affiche list ou <class 'list'>

ok=True
print(type(ok)) #affiche boolean ou <class 'bool'>

age=20
if age>=18:
    print('majeur pour age=',age)
    print('pas mineur')
print('suite dans tous les cas')

age=16
if age>=18:
	print('majeur pour age=',age)
else :
	print('mineur pour age=',age)
print('suite dans tous les cas')

age=30
if (age>=18) and (age<=42) :
	print('age entre 18 et 42 ans')
print('suite dans tous les cas')

age=16
if (age<18) or (age>=65) :
	print('enfant ou bien personne agée')
print('suite dans tous les cas')

liste_couleurs = [ 'rouge' , 'vert' , 'bleu' , 'noir' , 'blanc' ]
print('la taille de liste de couleurs est ' , len(liste_couleurs) )
print('la première couleur est ' , liste_couleurs[0] ) # affiche rouge
print('la couleurs du milieu est ' , liste_couleurs[2] )# affiche bleu
print('la dernière couleur est ' , liste_couleurs[4] )# affiche blanc
print('en dernier ' , liste_couleurs[len(liste_couleurs)-1] )#  blanc

seq=1,2,3
print('sequence 1, 2 , 3',seq, type(seq)) # s'affiche comme (1 , 2 , 3)

print('range(4)=de 0 à 3<4 =',list(range(4))) # affiche [ 0,1,2, 3 ]
print('range(3,6)=de 3 à 5<6 = ',list(range(3,6))) # affiche [ 3, 4 , 5 ]
print('range(4-1,0-1,-1)= séquence inversée = ',list(range(3,-1,-1))) # affiche [ 3, 2 , 1 , 0 ]

#indicesDe0a3= 0,1,2,3
indices_0a3= range(4) # range(4) construit 0, 1, 2, 3
for i in indices_0a3 :
	print("i=",i)
print('suite apres la boucle')

print('boucle de 2 à 8<9 par pas de 2 soit de 2 en 2 :');
for i in range(2,9,2) :
	print("i=",i)
print('suite apres la boucle')

jours_semaine = ['lundi','mardi','mercredi','jeudi','vendredi','samedi','dimanche']
# la liste (ou tableau) jours_semaine comporte 7 éléments dont les positions/indices vont de 0 à 6
for jour in jours_semaine :
	print(jour,'est un element de jours_semaine')
print('suite apres la boucle')

#nb_jours_dans_semaine=7
nb_jours_dans_semaine=len(jours_semaine) # la fonction len() retourne la taille/longueur (length en englais)
for i in range(nb_jours_dans_semaine) :
	print("i=",i,"jour=",jours_semaine[i])
print('suite apres la boucle')

liste =[ 10 , 40 , 30 , 50 , 20 ]
somme=0;
taille=len(liste)
for valElt in liste :
	somme=somme + valElt
moyenne=somme/taille;
print('somme=',somme) # affiche 150
print('moyenne=',moyenne) # affiche 30
	

"""
L'instruction if ne peut pas etre vide . si pour une raison quelconque
on souhaite y placer une instruction sans contenu , on peut utiliser l'instruction pass
pour éviter une erreur
"""
x1=5; x2=6
if x2 > x1 :
	pass # ne rien faire pour l'instant (version 1 temporaire)
print("suite apres if ne faisant rien pour l'instant")

age=33
etat="majeur" if age >=18 else "mineur"
# équivalent en c,c++,java,javascript: etat=(age>=18)?"majeur":"mineur"
print("etat=",etat , "pour age" , age) # etat= majeur pour age 33

age=15
etat="majeur" if age >=18 else "mineur"
print("etat=",etat, "pour age" , age) # etat= mineur pour age 15

x=25
if x >= 20:
	print("x >= 20")
	if x >= 30 :
		print("et aussi x >=30")
	else:
		print("et x < 30 (pas >= 30)")

heure=15

if heure<=12:
    print("bonjour!")
elif heure <=18 :
    print("bon après midi!")
else:
    print('bonsoir!')		

matrice = [
	[ 4 , 0 , 5] ,
	[ 2 , 6 , 1] ,
	[ 0 , 3 , 0]
]	

for i in range(3) :
	for j in range(3):
		print("matrice("+str(i)+","+str(j)+")=" , matrice[i][j])

s="abc"
for c in s:
	print("c=",c)

languages=["python" , "javascript"];
for l in languages:
	print("l=",l)
else:
	print("--- fin de liste ----")

valeurs=[-1, -8, 6 , -9 , 12,-3, 4]
premier_positif=None ; print("type de None=",type(premier_positif))
for v in valeurs:
	if v >=0 :
		premier_positif=v
		break # fin anticipée de boucle (premierPositif déjà trouvé)
print("premier_positif=",premier_positif) # 6

for v in valeurs:
	if v <0 :
		continue # passer directement à l'itération suivante
	print("positive v=",v) #instruction declenchée que si pas continue avant

age=33
#message = "mon age est " + age #TypeError: can only concatenate str (not "int") to str
message = "mon age est " + str(age)
print("message=",message)

couleur = "vert"
if couleur == "rouge" :
	print("red")
elif couleur=="vert" :
	print("green")
elif couleur=="bleu" :
	print("blue")
else:
	print("other color")

couleur = "bleu"
match couleur:
	case "rouge" :
		print("red")
	case "vert" :
		print("green")
	case "bleu" :
		print("blue")
	case _ :
		print("other color / default")	
		