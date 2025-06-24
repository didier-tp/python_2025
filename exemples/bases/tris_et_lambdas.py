nombres = [34, 7, 12, 6, 89]
print("nombres=",nombres)
nombres.sort()
print("après tri, nombres=",nombres)  #  [6, 7, 12, 34, 89]

nombres.sort(reverse=True)
print("après tri décroissant, nombres=",nombres)  #  [89, 34, 12, 7, 6]

liste =  [34, 8, 15, 6, 67]
liste_triee = sorted(liste) #créer une nouvelle liste triée , option possible: reverse=True
print("liste=",liste)
print("liste_triee=",liste_triee)

liste = [ 'France' , 'Allemagne' , 'Suede' , 'Espagne' , 'Italie']
print("liste=",liste)
liste_triee = sorted(liste) 
print("liste_triee=",liste_triee)

liste_pers = [
    { 'nom' : 'Dupond' , 'age' : 23 },
    { 'nom' : 'Zorro' , 'age' : 44 },
    { 'nom' : 'Anatole' , 'age' : 66 },
    { 'nom' : 'Laurent' , 'age' : 25 }
]

print("liste_pers=",liste_pers)
liste_pers_triee_par_noms = sorted(liste_pers, key = lambda p : p['nom']) 
print("liste_pers_triee_par_noms=",liste_pers_triee_par_noms)
liste_pers_triee_par_ages = sorted(liste_pers, key = lambda p : p['age']) 
print("liste_pers_triee_par_ages=",liste_pers_triee_par_ages)

##### filtrages et transformations (avec lambdas)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
nombres_pairs = list(filter(lambda x: x % 2 == 0, numbers))
# list() indispensable autour de filter() , sinon simple filter_object
print("nombres_pairs=",nombres_pairs) #  [2, 4, 6, 8]

nombres_plus_grands_que_4 = list(filter(lambda x: x>4 , numbers))
print("nombres_plus_grands_que_4=",nombres_plus_grands_que_4) # [5, 6, 7, 8]


fruits = ['pomme', 'orange', 'cerise' , 'poire']
print("liste de fruits=",fruits)
liste_lengths = list(map(lambda x: len(x), fruits))
# list() ou autre indispensable autour de map() , sinon simple map_object
print("de longueurs=",liste_lengths) #  [5, 6, 6, 5]

############# reduce et lambda

from functools import reduce

numbers = [5, 6, 2, 7]
print("numbers=",numbers)
total = reduce(lambda x, y: x + y, numbers)
print(f'The sum of the numbers is {total}.') #20