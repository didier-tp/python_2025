from e1_Personne import Personne

### utilisation de classe Personne    

defaultP=Personne()
print("defaultP=",defaultP)

p1=Personne("jean","Bon",33)
print("p1=",p1)
p1.incrementer_age()
print("apres .incrementer_age(), p1=",p1)
p1.nom="Aimare"
print("apres changement de nom, p1=",p1)

