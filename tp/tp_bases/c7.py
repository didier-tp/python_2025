import math

def calcul_mensualite_emprunt(montant , nb_mois , taux_annuel_pct):
    taux_mensuel = (taux_annuel_pct/100)/12
    mensualite=(montant*taux_mensuel) / ( 1 - math.pow(1+taux_mensuel,-nb_mois))
    return mensualite


mensualite = calcul_mensualite_emprunt(montant=100000 , 
                                       nb_mois=120 , 
                                       taux_annuel_pct=2.5) # 942.69
print("mesualite=",mensualite)