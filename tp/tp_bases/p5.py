liste = [ 12 , 48 , 32 , 8 , 24 ]
somme=0
i=0 # index ou position
while i < len(liste) :
    somme = somme + liste[i]
    i+=1; # i=i+1
moyenne=somme/len(liste)
print("somme=",somme," moyenne",moyenne)

saisons=["hiver" , "printemps" , "ete" , "automne" ]
saisonsMaj=[]
for val in saisons:
    valMaj = val.upper()
    saisonsMaj.append(valMaj)

print("saisonsMaj=",saisonsMaj)    

for val in saisons:
    valMaj = val.upper()
    print("valMaj=",valMaj)