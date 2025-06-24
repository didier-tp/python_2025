'''
principaux modes d'ouverture: 
    r: read 
	w:write / ré-écriture (écrasement)
	a : append (ajout à la fin)
	
le fichier est souvent créé en écriture s'il n'existe pas

modes secondaires d'ouverture : 
	b : binaire (ex: images , videos, ...) 
	t : texte
'''

f= open("data.txt","wt")
print("f=",f); # affiche le descripteur de fichier ouvert, par exemple :
#f= <_io.TextIOWrapper name='data.txt' mode='wt' encoding='cp1252'>
f.close() # fermeture du fichier

#ouvrir un nouveau fichier et écrire 2 lignes dedans:
f= open("data.txt","wt")
f.write("ligne1\n")
f.write("ligne2\n")
f.close();

#ré-ouvrir un fichier existant et ajouter 2 lignes dedans:
f= open("data.txt","at")
f.write("ligne3\n")
f.write("ligne4\n")
f.close();

#ré-ouvrir un fichier existant et charger son contenu d'un seul coup:
f= open("data.txt","rt")
toutLeContenu=f.read(); print(toutLeContenu);
f.close();

#ré-ouvrir un fichier existant et lire son contenu ligne par ligne:
f= open("data.txt","rt")
ligneLue="?"
while ligneLue :
	ligneLue=f.readline(); 
	if ligneLue.endswith("\n") :
		ligneLue=ligneLue[:-1]
	print(ligneLue);
f.close();

#ré-ouvrir un fichier existant et lire son contenu ligne par ligne:
f= open("data.txt","rt")
for ligneLue in f :
	if ligneLue.endswith("\n") :
		ligneLue=ligneLue[:-1]
	print(ligneLue);
f.close();

###### with keyword for automatic closing (as in try/except/FINALLY) ####

with open("data2.txt","wt") as f :
	f.write("ligne1\n")
	f.write("ligne2\n")
    # automatic f.close() even in case of exception


##################### Format JSON #################"

import json

#personne1 en tant que dictionnaire python :
personne1={
  "nom" : "Bon" ,
  "age" : 45 ,
  "fou" : False,
  "adresse" : {
         "rue" : "12 rue elle",
		 "codePostal" : "75008",
		 "ville" : "Paris" 
		 } ,
   "sports" : [ "velo" , "foot" ]
 }
 
#p1AsJsonString = json.dumps(personne1);
p1AsJsonString = json.dumps(personne1,indent=4);
print("p1AsJsonString=",p1AsJsonString)
with open("p1.json","wt") as f :
	f.write(p1AsJsonString)
	
#relecture du fichier p1.json et extraction du contenu en données python:
with open("p1.json","rt") as f :
	fileContentAsJsonString=f.read()
	pers = json.loads(fileContentAsJsonString)
	print("pers=",pers);
	print("type(pers)=",type(pers));


 