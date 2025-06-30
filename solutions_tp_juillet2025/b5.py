dico_produits={
    'fruit' : [ "banane" , "orange" , "pomme" ] ,
    'legume' : [ "carotte" , "choux" , "tomate"],
    'divers' : [ 'stylo' , 'cahier']
}
#supprimer la categorie de produits qui ne se mange pas
del dico_produits["divers"]

#afficher le dictionnaire complet:
print("dico_produits=",dico_produits)

#afficher la liste des clefs (categories):
print("categories de produits=",list(dico_produits.keys()))

#afficher la liste des fruits:
print("liste des fruits=",dico_produits['fruit'])

# transformer les noms des produits en majuscule
for categorie in dico_produits :
    for i in range(len(dico_produits[categorie])) :
        prod = dico_produits[categorie][i]
        prod=prod.upper()
        dico_produits[categorie][i]=prod
      

#ré-afficher le dictionnaire:
print("dico_produits=",dico_produits)        