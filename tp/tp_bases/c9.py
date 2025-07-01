liste_produits = [
{ 'id' : 1 , 'label' : 'cahier' , 'price' : 2.4 },
{ 'id' : 11 , 'label' : 'classeur' , 'price' : 4.4 },
{ 'id' : 2 , 'label' : 'stylo' , 'price' : 1.4 },
{ 'id' : 4 , 'label' : 'gomme' , 'price' : 2.41},
{ 'id' : 3 , 'label' : 'trousse' , 'price' : 5.4 },
]
print("liste_produits=",liste_produits)

liste_triee_par_prix = sorted(liste_produits , key = lambda p : p['price'])
print("liste_triee_par_prix=",liste_triee_par_prix)

liste_triee_par_label = sorted(liste_produits , key = lambda p : p['label']  )
print("liste_triee_par_label=",liste_triee_par_label)