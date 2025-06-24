import os

cwd = os.getcwd() 
print("Current working directory:", cwd) #  C:\tp\xyz

userHomeDirectory = os.path.expanduser("~")
print("userHomeDirectory:", userHomeDirectory) #  C:\Users\toto

try:
    #os.mkdir("mon_sous_repertoire") # créer un sous répertoire (si droits suffisants)
    print(os.listdir()) # affiche la liste du contenu du répertoire courant
    #os.rename("mon_sous_repertoire" , "my_sub_dir") # renommer un fichier ou répertoire (si droits suffisants)
    #print(os.listdir())
    #os.remove("my_sub_dir")# supprimer un fichier ou répertoire (si droits suffisants)
    #print(os.listdir)
except Exception as e:
    print("une exception a eu lieu:",e)

###########################

import sys
print("version de python=",sys.version) # ex 3.13.3 (...)
print("system platform=",sys.platform) # ex: win32
print("path=",sys.path) # seulement partie accessible depuis python
sys.exit(0); #fin du process en retournant le code 0