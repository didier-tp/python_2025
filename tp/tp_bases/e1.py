from e1_Personne import Personne

p1=Personne(prenom='jean',nom='Bon',age=44)
print("nom de p1=" ,p1.nom)
print("p1=",p1) # ou bien print("p1=",str(p1))

p2=Personne()
print("p2 avec valeurs par défaut=",p2)
p2.nom='Aimare'; p2.age=33
print("nom de p2=" ,p2.nom)
print("p2 avec changement de valeurs=",p2)
p2.incrementer_age()
print("p2 avec incrementer_age=",p2)