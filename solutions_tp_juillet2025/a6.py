nb_essais=0
a_deviner=33
x=None
while x!=a_deviner :
    x=int(input("x="))
    nb_essais+=1
    if x > a_deviner :
        print("trop grand")
    elif x < a_deviner :
        print("trop petit")
    else:
        print("vous avez trouvé " + str(a_deviner) + " en " + str(nb_essais) + " essais")