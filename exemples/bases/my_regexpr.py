import re

tab = [ "Durand" , "2a" , "toto" , "R2d2", "Dupond"]
for s in tab:
    matchTuple = (s , re.match(r"^[A-Z]\D" , s))
    print(matchTuple,end="\t")
    if matchTuple[1] :
        print (matchTuple[0] + " est un nom correct")
    else:
        print (matchTuple[0] + " n'est pas un nom correct")


allNumbers = re.findall(r"([0-9]+)", "Entre 001 et 999")
print("allNumbers=",allNumbers) #   ['001', '999']    

s1 = "12 8 16.8 9 -1"
print("s1=",s1)
s2 = re.sub(r"\s",r",",s1) #remplace les espaces par des virgules
print("s2=",s2) # "12,8,16.8,9,-1"