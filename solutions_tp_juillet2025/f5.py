# test de l'opérateur > ajouté sur la classe Compte dans e3_Compte.py

from e3_Compte import Compte

c1=Compte(1,"compte_a",150.0)
c2=Compte(2,"compte_b",60.0)

if c1 > c2 :
    print(" c1 est plus grand que c2 d'un point de vue solde courant")
else :
    print(" c1 n'est pas plus grand que c2 d'un point de vue solde courant")