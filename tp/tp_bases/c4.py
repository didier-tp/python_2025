def create_cercle_dict(rayon,xc,yc,couleur="black"):
    dict_cercle = { 'rayon' : rayon , 'xc' : xc , 'yc' : yc , 'couleur' : couleur}
    return dict_cercle

d1=create_cercle_dict(100,50,50,"red")
print("d1=",d1)

print(create_cercle_dict(1000,500,500,"green"))
print(create_cercle_dict(800,400,400))
print(create_cercle_dict(rayon=10,xc=500,yc=500,couleur="blue"))