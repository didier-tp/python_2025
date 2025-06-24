dictionnaire_vide={}
dictionnaire2 = dict()

#un dictionnaire python est une table d'association (Map)
#(ensemble de couples (clef,valeur))
#La syntaxe d'un dictionnaire python est très proche de JSON (javascript object notation)
dictionnaire_couleurs={
"red":"#ff0000",
"green":"#00ff00",
"blue":"#0000ff"
} 

rgbRed=dictionnaire_couleurs["red"];
print("rgbRed=",rgbRed); # #ff0000
dictionnaire_couleurs["red"]="#FF0000"; # change value 
print(dictionnaire_couleurs["red"]); # #FF0000

rgbGreen=dictionnaire_couleurs.get("green");
print("rgbGreen=",rgbGreen); # #00ff00

dictionnaire_couleurs["black"]="#000000"; # add new key and value 
print(dictionnaire_couleurs["black"]); # #000000

dictionnaire_couleurs.update({"white":"#FFFFFF"}); # add new {key : value } pair
print(dictionnaire_couleurs["white"]); # #FFFFFF

dictionnaire_couleurs.update({"white":"#ffffff" , "yellow" : "#ffff00"}); # fusionner autre dictionnaire
print(dictionnaire_couleurs["yellow"]); # #ffff00

del dictionnaire_couleurs["white"]; #ou bien dictionnaire_couleurs.pop("white")
print(dictionnaire_couleurs); # {'red': '#FF0000', 'green': '#00ff00', 'blue': '#0000ff', 'black': '#000000', 'yellow': '#ffff00'}

dico_pers= { "nom" : "Bon" , "age" : 45 }
print("nom=" + dico_pers.get("nom")); # Bon
print("nom=" + dico_pers.get("prenom","prenomParDefaut")); # prenomParDefaut

dico_pers= { "nom" : "Bon" , "age" : 45 }
for key in dico_pers :
	print(key)
# nom
# age

dico_pers= { "nom" : "Bon" , "age" : 45 }
for clef in dico_pers.keys() :
	print(clef)
# nom
# age

for val in dico_pers.values() :
	print(val)
# Bon
# 45

for clef,val in dico_pers.items() :
	print(clef,val)
# nom Bon
# age 45

dico_pers= { "nom" : "Bon" , "age" : 45 }
print("nbAssociations=" , len(dico_pers)) # 2
dico_duplique=dico_pers.copy(); #ou bien dico_duplique=dict(dicoPers);
dico_duplique["age"]=30
print(dico_pers) # { "nom" : "Bon" , "age" : 45 }
print(dico_duplique) # { "nom" : "Bon" , "age" : 30 }

dico_duplique.clear() # vide le contenu du dictionnaire

if "nom" in dico_pers:
	print("dico_pers comporte la clef nom")
else :
	print("dico_pers ne comporte pas la clef nom")
	
#NB: au sein d'un dictionnaire une valeur peut être 
#une liste ou un dictionnaire imbriqué:
dico_pers={
  "nom" : "Bon" ,
  "age" : 45 ,
  "fou" : False,
  "adresse" : {
         "rue" : "12 rue elle",
		 "codePostal" : "75008",
		 "ville" : "Paris" 
		 } ,
   "sports" : [ "vélo" , "foot" ]
 }
print("dico_pers très proche du format JSON:" , dico_pers);


