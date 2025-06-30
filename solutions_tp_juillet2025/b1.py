l1=[ -1, 2 , -8 , 7 , 4 , 3 , -9 , 9 , 12 , -5 , 5]
positifs=[]
impairs=[]
for v in l1 :
    if v>=0 :
        positifs.append(v)
    if v%2!=0 :
        impairs.append(v)
print("valeur positives=",positifs)
print("valeur impaires=",impairs)

noms = [ "jean" , "Luc" , "eric" , "Julie" ]
for nom in noms :
    #nom_maj = nom.upper()
    #if nom[0] != nom_maj[0] :
    if nom[0].islower() :
        noms.remove(nom)
print("noms=",noms)     
