import datetime
import random

f= open("my_fic.txt","wt")

maintenant = datetime.datetime.now()

s_date_fr=maintenant.strftime("%d/%m/%Y")
ligneDate=f"date:{s_date_fr}\n"
f.write(ligneDate)

s_heure_fr=maintenant.strftime("%H:%M:%S")
ligneHeure=f"heure:{s_heure_fr}\n"
f.write(ligneHeure)

nb_alea_entre_1_et_100=random.randint(1,100)
ligneAlea=f"aleatoire:{nb_alea_entre_1_et_100}\n"
f.write(ligneAlea)

f.close()