liste_vide=[]

liste_initiale=[1,2,3]

liste=liste_initiale
liste.append(4)
print("liste=",liste) # affiche [1,2,3,4]
print("liste=",liste)

print("premier élément:",liste[0]) # affiche 1
liste[0]=1.1
print("premier élément modifié:",liste[0]) # affiche 1.1
#liste[4]=5  --> IndexError: list assignment index out of range
print("dernier élément:",liste[-1]) # affiche 4 (dernier élément)


liste2 = [ "a" , "b" , "c" ]
del liste2[1] # suppression de l'élément d'indice 1 (0,1,2)
print("liste2=",liste2) # affiche [ 'a' , 'c' ]

liste3 = [ "rouge" , "vert" , "bleu" ]
liste3.remove("vert") # suppression de l'élément dont la VALEUR est "vert"
print("liste3=",liste3) # affiche [ 'rouge' , 'bleu' ]

liste4=[1,2,3,4];
liste4.reverse() # inverse l'ordre des éléments de la liste
print("liste4=",liste4) # affiche [ 4,3,2,1 ]

nb_elements=len(liste4)
print("longueur (nbElements) de liste4=",nb_elements) # affiche 4

liste5=['a' , 'b' , 'a' , 'b' , 'c' , 'a' ]
nb_occurences_a = liste5.count('a')
print("nb occurences de 'a' dans liste5=",nb_occurences_a) # affiche 3

indice_b_dans_liste5= liste5.index('b') 
print("indice_b_dans_liste5",indice_b_dans_liste5) # 1 (premier trouvé)

indice_c_dans_liste5= liste5.index('c')
print("indice_c_dans_liste5",indice_c_dans_liste5) # 4 

autre_liste = [ 'a' , 'b' , 'c1', 'd' , 'e']
autre_liste.insert(3,'c2') #insertion avant l'élément actuel d'indice 3
                          #insertion du nouvel élément en pos 3 et en décalant la fin
print('autre_liste apres insertion:' , autre_liste)

#liste5.index('e') --> ValueError: 'e' is not in list

liste = [ 'a' , 'b', 'c' ]

#boucle sur indices:
for i in range(len(liste)) :
	print('i=',i,'liste[i]=',liste[i])
# i= 0 liste[i]= a
# i= 1 liste[i]= b
# i= 2 liste[i]= c


liste = [ 'a' , 'b', 'c' ]

#boucle sur valeur des éléments:
for val in liste :
	print(val)
# a 
# b
# c

#boucle sur indices et valeurs des éléments:
for tuple_indice_val in enumerate(liste) :
	print(tuple_indice_val , tuple_indice_val[0] , tuple_indice_val[1] )
# (0,'a') 0 a 
# (1,'b') 1 b
# (2,'c') 2 c

liste6 = [ 2 , 4 , 6 ]
refListe = liste6 # refListe référence la même liste que celle référencée par liste6
refListe[0]=2.2 # même effet que liste6[0] = 2.2
print("liste6=",liste6) # affiche [ 2.2 , 4 , 6 ]

liste7 = [ 1 , 3 , 5]
liste8 = liste7.copy() # copie/duplication d'une liste simple
liste8[0]=1.1
print("liste7=",liste7) # affiche [1, 3 , 5]
print("liste8=",liste8) # affiche [1.1, 3 , 5 ]

ma_pile = [ 1 , 2 ,  3 , 4]
dernier_element_retire  = ma_pile.pop(); print(dernier_element_retire); # 4
dernier_element_retire  = ma_pile.pop(); print(dernier_element_retire); # 3
print(ma_pile); # [ 1, 2 ]

trois_couleurs="rouge;vert;bleu" # grande chaîne de caractères avec sous parties séparées par ";"
liste_couleurs = trois_couleurs.split(";")
print("liste_couleurs=",liste_couleurs) # ['rouge', 'vert', 'bleu']

mes_couleurs=";".join(liste_couleurs) # transforme liste en chaîne de caractères
print("mes_couleurs=",mes_couleurs) # affiche la chaîne rouge;vert;bleu


liste10=[ 'a' , 'b' , 'c' ]
if 'a' in liste10 :
	print('liste10 comporte a')
else :
	print('liste10 ne comporte pas a')
	
if 'd' in liste10 :
	print('liste10 comporte d')
else :
	print('liste10 ne comporte pas d')	


'''
liste_couleurs =           [ 'rouge' , 'vert' , 'bleu' , 'noir' , 'blanc' ]
# indices ou positions :      0            1        2        3        4
print('la taille de liste de _couleurs est ' , len(liste_couleurs) ) # affiche 5
print('la première couleur est ' , liste_couleurs[0] ) # affiche rouge
print('la _couleurs du milieu est ' , liste_couleurs[2] ) # affiche bleu
print('la dernière couleur est ' , liste_couleurs[4] ) # affiche blanc
print('en dernier ' , liste_couleurs[ len(liste_couleurs)-1 ] ) #  blanc

print('plage 1 inclus à 3 exclus :' , liste_couleurs[1:3]) # ['vert', 'bleu']
print('plage début à 3 exclus :',liste_couleurs[:3]) # ['rouge', 'vert', 'bleu']
print('plage 2 inclus à fin  :',liste_couleurs[2:]) # ['bleu', 'noir', 'blanc']
'''