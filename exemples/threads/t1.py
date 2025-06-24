import threading
import time;

def tache1():
    print(">>> tache1: préparer du café")
    time.sleep(4) #4s de pause
    print(">>> tache1: le café est prêt")

    

# Création d'un nouveau thread secondaire
mon_thread = threading.Thread(target=tache1)
mon_thread.start() # démarrage du thread secondaire

#actions effectuées en // par le thread principal:
print("action1 effectuée par le thread principal")
time.sleep(1) #1s de pause
print("action2 effectuée par le thread principal")

# Attente de la fin de l'execution du thread secondaire
mon_thread.join()

print("fin de l'ensemble de lapplication python")