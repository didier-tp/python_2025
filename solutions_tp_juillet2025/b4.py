values = [ -2 , -7 , 2 , 8 , -9 , 10 , 1 , 3 , -3 , 5]
dico_stats = { 'nb_positif' : 0 , 'nb_negatif' : 0 ,
             'nb_pair' : 0 , 'nb_impair' : 0 ,
             'taille' : 0 , 'somme' : 0}

dico_stats['taille']=len(values)
for v in values:
    dico_stats['somme']+=v
    if v>=0 :
        dico_stats['nb_positif']+=1
    else:
        dico_stats['nb_negatif']+=1
    if (v%2)==0 :
        dico_stats['nb_pair']+=1
    else:
        dico_stats['nb_impair']+=1

print("dico_stats=" , dico_stats)