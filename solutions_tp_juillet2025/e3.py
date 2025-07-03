from e3_Compte import Compte

### utilisation de la classe Compte    

defaultCompte=Compte()
print("defaultCompte=",defaultCompte)

c1=Compte(1,"compte_a",50.0)
print("c1=",c1)
c1.crediter(20)
c1.crediter(20)
print("apres deux appels de .crediter(20), c1=",c1)
c1.debiter(60)
print("apres .debiter(60), v1=",c1)


