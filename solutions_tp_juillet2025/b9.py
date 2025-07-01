liste_dico_dates =[
    { 'jour' : 4 , 'mois' : 'avril' , 'annee' : 2024} ,
    { 'jour' : 12 , 'mois' : 'juin' , 'annee' : 2023} ,
    { 'jour' : 22 , 'mois' : 'octobre' , 'annee' : 2025} ,
]

# construire et afficher des dates sous forme de chaines (via .format() )

for dico_date in liste_dico_dates :
    s_date = "{0} {1} {2}".format(dico_date['jour'] , dico_date['mois'] , dico_date['annee'] )
    print("s_date=",s_date)

#recuperer et afficher date_et_heure (maintenant):
import datetime

d = datetime.datetime.now()
print("maintant=",d)    