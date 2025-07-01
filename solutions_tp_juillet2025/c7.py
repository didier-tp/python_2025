import math
def calcul_mensualite_emprunt(montant,nb_mois,taux_annuel_pct ):
    taux_annuel = taux_annuel_pct / 100
    taux_mens = taux_annuel/12 
    return (montant * taux_mens) / (1-math.pow(1+ taux_mens,-nb_mois))

mensualite = calcul_mensualite_emprunt(montant=100000 , nb_mois=120 , taux_annuel_pct=2.5) # 942.69
print("mensualite=",mensualite)