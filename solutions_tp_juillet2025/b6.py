liste_pays=[
    { 'nom':'France'    , 'capitale' : 'Paris'  , 'population': 66352469  },
    { 'nom':'Allemagne' , 'capitale' : 'Berlin' , 'population': 81174000  },
    { 'nom':'Espagne'   , 'capitale' : 'Madrid' , 'population': 46439864  },
    { 'nom':'Italie'    , 'capitale' : 'Rome'   , 'population': 60795612  },
    { 'nom':'Royaume-Uni', 'capitale' :'Londres', 'population': 64767115  },
]
#calculer et afficher la population totale:
population_totale=0
for p in liste_pays:
    population_totale+=p['population']

print('population totale=',population_totale)    