from e3_Compte import Compte

c1=Compte(1,"compte1",50.0)
c1.debiter(20) # pour déclencher Compte.debiter(self=c1,montant=20)
#devrait rester un solde de 30.0
print("c1=",c1)