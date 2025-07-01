from functools import reduce

liste_produits = [
    { 'id' : 1 , 'label' : 'cahier' , 'price' : 2.4 },
    { 'id' : 11 , 'label' : 'classeur' , 'price' : 4.4 },
    { 'id' : 2 , 'label' : 'stylo' , 'price' : 1.4 },
    { 'id' : 4 , 'label' : 'gomme' , 'price' : 2.41},
    { 'id' : 3 , 'label' : 'trousse' , 'price' : 5.4 },
]
prix_max=4
liste_filtree = list(filter( lambda p: p['price'] <= prix_max, liste_produits))
print("liste_filtree=",liste_filtree)

liste_prix=list(map(lambda p: p['price'], liste_filtree))
print("liste_prix=",liste_prix)

prix_total=reduce(lambda p1,p2: p1 + p2, liste_prix)
print("liste_total=",prix_total)