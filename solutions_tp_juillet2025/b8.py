nom_fichiers=[ "fichierA.txt" , "configB.json" , "b8.py" ]
# boucler sur chaque nom complet de fichier
# et afficher séparément nom et extension 
for nom_fic in nom_fichiers:
    pos_point=nom_fic.find('.')
    print("nom_fic=",nom_fic,"pos_point=",pos_point)
    nom=nom_fic[0:pos_point] # [0,pos_point[
    extension=nom_fic[pos_point+1:len(nom_fic)] 
    print("nom=",nom,"extension=",extension)

#variante de la solution:
for nom_fic in nom_fichiers:
    liste_parties=nom_fic.split(".")
    print("nom_fic=",nom_fic,"liste_parties=",liste_parties)
    nom=liste_parties[0]
    extension=liste_parties[1]
    print("nom=",nom,"extension=",extension)