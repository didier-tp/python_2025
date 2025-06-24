l1 = [ 12 , 48 , 32 , 8 , 24 ] 
somme=0
taille=len(l1)
'''
for i in range(taille):
    somme += l1[i]
'''
i=0
while i < taille :
    somme += l1[i]
    i+=1

l2 = [ 12 , 48 , 32 , 8 , 24 ] 
somme=0
for val in l2:
    somme += val

print('somme de l2=',somme)
print('moyenne de l2=',somme/len(l2))

saisons = ["hiver" , "printemps" , "ete" , "automne" ]
saisonsMaj = []
for i in range(len(saisons)):
    saisonsMaj.append(saisons[i].upper())
    
print("saisonsMaj=",saisonsMaj)    