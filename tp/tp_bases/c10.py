import functools

liste_produits = [
{ 'id' : 1 , 'label' : 'cahier' , 'price' : 2.4 },
{ 'id' : 11 , 'label' : 'classeur' , 'price' : 4.4 },
{ 'id' : 2 , 'label' : 'stylo' , 'price' : 1.4 },
{ 'id' : 4 , 'label' : 'gomme' , 'price' : 2.41},
{ 'id' : 3 , 'label' : 'trousse' , 'price' : 5.4 },
]

liste_produits_pas_chers = list(filter(lambda p: p['price'] <= 4, liste_produits))
print("liste_produits_pas_chers=", liste_produits_pas_chers)

liste_prix_produits_pas_chers = list(map(lambda p :p['price'], liste_produits_pas_chers))
print("liste_prix_produits_pas_chers=", liste_prix_produits_pas_chers)

prix_total = functools.reduce(lambda x, y: x + y, liste_prix_produits_pas_chers)
print(f'prix_total= {prix_total}') # 6.21
