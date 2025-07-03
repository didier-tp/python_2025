from e4_Employe import Employe

e1=Employe(prenom="jean" , nom="Bon" , age=40 ,salaire=2500 , fonction="developpeur")
print("e1=",e1)
e1.incrementer_age() #on peut appeler n'importe quelle méthode héritée même si pas reprogrammée sur classe Employe
print("e1 avec un an de plus =",e1)

e1.decrire() # avec print() sur la console texte