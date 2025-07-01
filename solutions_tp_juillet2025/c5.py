def mon_maxi(*args):
    nb_args=len(args)
    if nb_args==0 :
        return 0
    else :
        max = args[0]
        for i in range(1,nb_args):
            if args[i] > max:
                max=args[i] 
        return max
    
#print(mon_maxi())
print(mon_maxi(12,6,89,3))
print(mon_maxi(8,3,9,4,23,7,12))

def display_carre(**kwargs):
    for k,v in kwargs.items():
        c=v*v
        print(f"{k}={v} , carre({k})={c}")

display_carre(x=6,y=9)      # x=6 , carre(x=36)    y=9 , carre(y=81)
display_carre(x=2,y=4,z=6)  # x=2 , carre(x=4)     y=4 , carre(y=16)   z=6 , carre(z=36)     