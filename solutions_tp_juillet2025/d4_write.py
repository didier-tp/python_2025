import datetime
import random
maintenant=datetime.datetime.now()
date = maintenant.strftime("%d/%m/%Y")
heure = maintenant.strftime("%H:%M:%S")
aleatoire=random.randint(0, 100)

f=open("my_fic.txt","wt")
f.write("date:" + date + "\n")
f.write("heure:" + heure  + "\n")
f.write("aleatoire:" + str(aleatoire) )
f.close()