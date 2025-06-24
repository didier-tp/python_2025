x=0
while x <= 5 :
	print ('x=',x,'x*x=',x*x)
	x=x+1
print('suite apres la boucle')

liste_couleurs = [ "rouge" , "noir" ]
liste_couleurs.append("vert") # ajoute l'élément "vert" à la liste
liste_couleurs.append("bleu") # ajoute l'élément "bleu" à la liste
print("liste_couleurs=",liste_couleurs); # ['rouge', 'noir', 'vert', 'bleu']

#NB: un paquet de ligne de code encadré par ''' et '''
#    sont considérées comme 'en commentaire' et donc pas déclenchées/exécutées
'''
liste_valeurs = []
valeur_ou_fin=input("val=")
while (valeur_ou_fin != 'fin' ) and (valeur_ou_fin != '' ):
	nouvelleValeur = float(valeur_ou_fin)
	liste_valeurs.append(nouvelleValeur)
	valeur_ou_fin=input("val=")
print('liste_valeurs=',liste_valeurs)
'''

nom="toto"
nom=nom.upper() # retourne la chaine transformée avec des caractères majuscules
print(nom) # affiche TOTO

saisons = ["hiver" , "printemps" , "ete" , "automne" ] 
for i in range(len(saisons)) :
    s = saisons[i]
    saisons[i]=s.upper()
print(saisons)
