s1="Hello"
s2=' World'
s3=s1+s2 #concatenation
print(s3) # Hello World

s4='''ile de
france'''
print(s4) # affiche une chaine multi-lignes

s5="Bonjour"
premier_caractere=s5[0]
print(premier_caractere) # B

dernier_caractere=s5[-1]
print(dernier_caractere) # r

# [i,j] means .substring(i,j) included i and excluding j

trois_premiers_caracteres=s5[0:3]# s5[0:3] means s5[0:3[ !!!
print(trois_premiers_caracteres) # Bon

n=len(s5) # length of string (7)

trois_derniers_caracteres=s5[n-3:n]# s5[n-3:n] means s5[n-3:n[ !!!
print(trois_derniers_caracteres) # our

s6=" Ile De France "
s6__bis=s6.strip() #like trim of other language --> supprime espaces inutiles
                 #au début ou à la fin
print(s6__bis) # "Ile De France"

s7="Mont Saint Michel"
s7_maj = s7.upper(); print(s7_maj) # MONT SAINT MICHEL 
s7_min = s7.lower(); print(s7_min) # mont saint michel

s7="Mont Saint Michel"
s7_bis=s7.replace(' ','-'); # replace substring with another string
print(s7_bis) # Mont-Saint-Michel

s8="partie1;partie2;partie3"
liste_parties=s8.split(';')
print(liste_parties) # ['partie1', 'partie2', 'partie3']

s9="un deux trois"
if "deux" in s9 :
	print("s9 comporte deux")
else :
	print("s9 ne comporte pas deux")

#il existe aussi le test if "deux" not in s9 

nom="toto"
age=30
taille=1.80
#.format remplace {0} , {1} , {2} , ... par les 1er,2eme,3eme arguments
description="{0} a {1} an(s) et mesure {2} m".format(nom,age,taille)
print(description) # toto a 30 an(s) et mesure 1.8 m

#caractères spéciaux : \n = new line , \t = tabulation , ...
#escape : \\ means \ 

s10="\tHello" ; print(s10); #      Hello
s11="surLigne1\nsurLigne2" ; print(s11); 
# surLigne1
# surLigne2

s12="dupond";
s12_bis=s12.capitalize() # transforme première lettre en _majuscule
print(s12_bis); # Dupond

file_name="p2.py"
dot_index = file_name.find(".") 
# .index() retourne position de la chaine recherchée et erreur si pas trouvée
# .find() retourne position de la chaine recherchée et -1 si pas trouvée
print("position . =" , dot_index) # 2

s13="phrase finissant par un point."
if s13.endswith(".") :
	print("s13 se ter_mine par '.' ")
	
s14="123"
if s14.isdigit() :
	print("s14 ne comporte que des caractères numériques ")
	
##### f-string depuis python 3.6

nom="toto"
age=30
taille=1.80

message = f'{nom} a {age} ans et mesure {taille} m'
print("message=",message) # toto a 30 ans et mesure 1.8 m

pers = { 'nom' : 'titi' , 'age' : 40 , 'taille': 1.66}
message = f'{pers["nom"]} a {pers["age"]} ans et mesure {pers["taille"]} m'
print("message=",message) # titi a 40 ans et mesure 1.66 m