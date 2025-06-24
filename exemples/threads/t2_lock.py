import threading
import time;

compteur_partage=0
verrou_global = threading.Lock()

def incrementer(num_thread):
    compteur_local=0
    global compteur_partage
    for _ in range(10):
        with verrou_global:
            compteur_local +=1
            compteur_partage +=1
            print(f"compteur_partage={compteur_partage} venant d'etre incrementé par t{num_thread} , compteur_local={compteur_local}")



# Création de plusieurs threads
mes_threads = [threading.Thread(target= incrementer, args=[num_t+1]) for num_t in range(5)]

for t in mes_threads :
    t.start() # démarrage des threads secondaires


for t in mes_threads :
    # Attente de la fin de l'execution d'un thread secondaire
    t.join()

print("fin de l'ensemble de lapplication python, compteur_partage=",compteur_partage)