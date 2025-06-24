ensemble_vide={}

#dans un ensemble, les éléments ne sont pas ordonnés (sans index stables)
ensemble_fruits={"apple", "banana", "cherry"} 

print("ensembleDeFruits=",ensemble_fruits) #  {'banana', 'cherry', 'apple'}

for f in ensemble_fruits:
  print(f)
#banana
#cherry
#apple

#NB: une fois qu'un ensemble a été créé/initialisé , on ne peut pas modifier
# ses éléments mais on peut ajouter un nouvel élément via .add()
# ou bien de nouveaux éléments via .update()

ensemble_fruits.add("orange") # ajout (sans notion d'ordre)
print(ensemble_fruits) # {'apple', 'orange', 'banana', 'cherry'}

ensemble_fruits={"apple", "banana", "cherry"}
ensemble_fruits.update({"orange" , "peach"}) # ajout de plusieurs éléments
print(ensemble_fruits) # {'apple', 'peach', 'banana', 'orange', 'cherry'}

ensemble_fruits={"apple", "banana", "cherry"}
ensemble_fruits.remove("banana") # supprime un élément s'il existe , erreur sinon
print(ensemble_fruits)  # {'cherry', 'apple'}
ensemble_fruits.discard("banana") # supprime un élément s'il existe toujours sans erreur 

ensemble_fruits.clear() # vide l'ensemble
print(ensemble_fruits)  # {}

set1 = {"a", "b" , "c"}
set2 = {"d", "e", "f"}

set3 = set1.union(set2)
print(set3) # {'b', 'd', 'a', 'e', 'c', 'f'}

set4 = {"a", "b" , "c" , "d"}
set5 = {"c", "d" , "e" , "f"}

set6 = set4.intersection(set5)
print(set6) # {'d', 'c'}

#il existe également .isdisjoint() , .issubset() , .difference() , ...

# transformations de set en liste , tuple et vice versa
set1 = {"a", "b" , "c"  }
liste_from_set1 = list(set1)
print("listeFromSet1",liste_from_set1,type(liste_from_set1))



tuple1 = ("a", "doublon", "b" , "c" , "doublon")
set_from_tuple1 = set(tuple1)
print("set_from_tuple1 =", set_from_tuple1 ,type(set_from_tuple1))

tuple2 = ("a", "b" , "c"  )
liste_from_tuple2 = list(tuple2)
print("liste_from_tuple2",liste_from_tuple2,type(liste_from_tuple2))