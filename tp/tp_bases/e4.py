from e4_Employe import Employe
from e1_Personne import Personne
e1=Employe(prenom="jean" , nom="Bon" , age=40 ,salaire=2500 , fonction="developpeur")
print("e1=",e1)
e1.incrementer_age() #on peut appeler n'importe quelle méthode héritée même si pas reprogrammée sur classe Employe
print("e1 avec un an de plus =",e1)

e1.decrire() # avec print() sur la console texte

listePersonnes=[]
listePersonnes.append(e1)
listePersonnes.append(Employe("alex","Therieur",20,3000,"data analyst"))
listePersonnes.append(Personne("axelle","Aire",25))
listePersonnes.append(Personne("alain","Therieur",35))
listePersonnes.append(Employe("luc","Xyz",20,3000,"commercial"))
print("------- liste des personnes----")
for p in listePersonnes:
    p.decrire()
    '''
    if isinstance(p,Employe):
        print(f" {p.nom} est un employe")
    else:
        print(f" {p.nom} est un personne ordinaire")
    '''