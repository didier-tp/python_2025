from e1_Personne import Personne

p1=Personne("jean","Bon",33)
print("p1=",p1)

try:
    p1.age = -40
    print("p1=",p1)
except ValueError as e:
    print("exception:",e)

p1.age = 28
print("nouvel age de p1=",p1.age)

