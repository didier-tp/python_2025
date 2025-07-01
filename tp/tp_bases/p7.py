def calcul_somme_et_aff_prefixe(x,y,prefixe=">>"):
    somme = x+y
    print(prefixe+ str(somme))

calcul_somme_et_aff_prefixe(5,6,"**")

calcul_somme_et_aff_prefixe(4,8,"##")

calcul_somme_et_aff_prefixe(4,8)

calcul_somme_et_aff_prefixe(prefixe ="***", x= 4, y=8)


########## éventuelles précisions sur types des paramètres et types des valeurs de retour #######
#### NB: à l'exécution du code , l'interpréteur python n'en tient pas compte
####     ça sert essentiellement à paramétrer des extensions pythons qui 
####     interprète cela (ex: aide lors de l'écriture d'un appel de fonction au niveau de l'IDE)

def greeting(name : str  ='?') -> str:
    #return 'Hello ' + name
    return 'Hello ' + str(name)

print(greeting("toto"))
print(greeting(5))
print(greeting())

