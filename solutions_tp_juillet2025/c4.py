def create_cercle_dict(rayon,xc=0,yc=0,couleur="black"):
    return {
        'rayon' : rayon,
        'xc':xc,
        'yc':yc,
        'couleur':couleur
    }

print(create_cercle_dict(50,20,20,"red")) # {'rayon': 50, 'xc': 20, 'yc': 20, 'couleur': 'red'}
print(create_cercle_dict(50,60,80)) # {'rayon': 50, 'xc': 60, 'yc': 80, 'couleur': 'black'}
print(create_cercle_dict(50, couleur="blue")) # {'rayon': 50, 'xc': 0, 'yc': 0, 'couleur': 'blue'}
print(create_cercle_dict(rayon=50,couleur="green")) # {'rayon': 50, 'xc': 0, 'yc': 0, 'couleur': 'green'}