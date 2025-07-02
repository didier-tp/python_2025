import os
import sys

if len(sys.argv)>1 :
    repertoire = sys.argv[1] #nom de réperoire éventuellement passé en argument de d5.py
else:
    repertoire = input("nom ou chemin de répertoire à analyser : ")

if repertoire=="":
    repertoire="." #par defaut repertoire courant
    
print(f"repertoire={repertoire}")
liste_contenu = os.listdir(repertoire)

taille_maxi=-1
taille_mini=sys.maxsize
smaller="?"
bigger="?"
taille_totale=0
nb_fichiers=0

for c in liste_contenu:
    c=os.path.join(repertoire,c) #complete path with "\" separator (ok for linux or windows)
    #if not os.path.isdir(c):
    if os.path.isfile(c):
        nb_fichiers +=1
        taille = os.path.getsize(c)
        taille_totale+=taille
        if taille > taille_maxi :
            taille_maxi=taille; bigger=c
        if taille < taille_mini:
            taille_mini=taille; smaller=c

print(f'nombre de fichiers: {nb_fichiers}')
print(f'taille totale: {taille_totale}')
print(f'plus petit fichier: {smaller} de taille {taille_mini}')
print(f'plus grand fichier: {bigger} de taille {taille_maxi}')

