
from e1_Personne import Personne
from e4_Employe import Employe

##### utilisation de la classe Employe heritant de Personne


e1=Employe("jean","Bon",33)
print("e1=",e1)   

e2=Employe("jean","Aimare",age=33,fonction="developpeur",salaire=2500.0)
print("e2=",e2) 

p1=Personne("alex","Therieur",25)
print("p1=",p1)

e3=Employe("axelle","Aire",age=42,fonction="analyste",salaire=3000.0)
print("e3=",e3) 

listePers = []
listePers.append(e1);listePers.append(e2)
listePers.append(p1);listePers.append(e3)

print("\nAffichages via .print() et .__str__() :")
for p in listePers:
    print("p=",p)

print("\nAffichages via .decrire() :")
for p in listePers:
    p.decrire()    