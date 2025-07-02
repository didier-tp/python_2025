#ré-ouvrir un fichier existant et lire son contenu ligne par ligne via boucle for :
f= open("my_fic.txt","rt")
for ligneLue in f :
    if ligneLue.endswith("\n") :
        ligneLue=ligneLue[:-1]
    print("**"+ligneLue+"**" , end=None)
f.close() 