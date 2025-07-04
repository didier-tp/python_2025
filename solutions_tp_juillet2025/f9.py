import re
tab_ref_prod = [ "Aa123xy" , "bb7ttt" , "ab674Ua" , "45yy", "au5" , "ry345yxt" , "zy145Yx"]

for ref in tab_ref_prod:
    matchTuple = (ref , re.match(r"^[a-zA-Z]{2}\d{3}[a-zA-Z]{2}$" , ref))
    #print(matchTuple)
    if matchTuple[1] :
        print (matchTuple[0] + " EST une référence de produit CORRECTE")
    else:
        print (matchTuple[0] + " n'est PAS correcte pour une référence de produit")