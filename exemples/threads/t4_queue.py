import threading
import queue
import time

# Création d'une file de données produites/consommées
#  qui sera vue par les différents threads avec verrouillage/syncro automatique
myQueue = queue.Queue()

def producteur(iMinInc=0,iMaxExcl=5):
    for i in range(iMinInc,iMaxExcl):
        curr_thread = f"thread_{threading.current_thread().ident}"
        print(f"Sending/Producing {i} in myQueue by {curr_thread}")
        myQueue.put(i)
        time.sleep(1)

def consommateur():
    while True:
        item = myQueue.get()
        curr_thread = f"thread_{threading.current_thread().ident}"
        square = item * item
        print(f"Receiving/Consuming {item} in myQueue by {curr_thread} , square={square}")
        myQueue.task_done()

# Création des threads
thread_producteur1 = threading.Thread(target=producteur,args=[1,4])
thread_producteur2 = threading.Thread(target=producteur,args=[6,9])

thread_consommateur = threading.Thread(target=consommateur, daemon=True) 
#deamon=True pour accepter fin du thread consommateur même le(s) dernier(s) élément(s) extrait(s)
#  de la file n'a/ont pas été entièrement traité(s)

# Démarrage des threads
thread_producteur1.start(); thread_producteur2.start()
thread_consommateur.start()

# Attente de la fin des producteurs
thread_producteur1.join();thread_producteur2.join()

myQueue.join()  # Attente jusqu'à ce que toutes les tâches soient consommées