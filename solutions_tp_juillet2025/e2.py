from e2_Voiture import Voiture

### utilisation de Voiture    

defaultV=Voiture()
print("defaultV=",defaultV)

v1=Voiture("Peugeot","208","red")
print("V1=",v1)
v1.accelerer(20)
v1.accelerer(20)
print("apres deux appels de .accelerer(20), v1=",v1)
v1.ralentir(30)
print("apres .ralentir(30), v1=",v1)

v2=Voiture("Renault","clio","green",75)
print("v2=",v2)

