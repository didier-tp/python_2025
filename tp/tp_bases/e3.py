from e3_Compte import Compte

c1=Compte(1,"compte1",50.0)
c1.debiter(20) # pour déclencher Compte.debiter(self=c1,montant=20)
#devrait rester un solde de 30.0
print("c1=",c1)

c2=Compte(2,"compte2LeRetour" , 150.0)
c2.crediter(30)
print("solde de c2=",c2.solde) # solde attendu 150+30=180