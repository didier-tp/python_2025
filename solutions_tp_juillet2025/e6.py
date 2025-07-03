from e6_Porte import Porte,PortePivotante,PorteCoulissante

'''
#TypeError: Can't instantiate abstract class Porte without an implementation
#  for abstract methods 'fermer', 'ouvrir', 'type_porte
porte_abstraite=Porte("porte abstraite impossible à instancier")
print("porte_abstraite=",porte_abstraite)
'''

listePortes=[]
listePortes.append( PorteCoulissante("porte1",fermee=True))
listePortes.append( PortePivotante("porte2",fermee=True))
listePortes.append( PorteCoulissante("porte3",fermee=True))
listePortes.append( PortePivotante("porte4",fermee=True))

#ouvrir toutes les portes:
for p in listePortes:
    p.ouvrir() # porte , ouvre toi !!! sans avoir a connaitre le type de porte

#afficher toutes les portes
for p in listePortes:    
    p.decrire()