from concurrent.futures import ThreadPoolExecutor
import time
import threading

def tache_longue(duree):
    curr_thread = f"thread_{threading.current_thread().ident}" #python 3
    print(f"Début tâche longue exécutée par {curr_thread} pendant {duree} secondes ")
    time.sleep(duree)
    return f"Fin tâche longue exécutée par {curr_thread}"

# Création d'un ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=3) as executor:
    durees_args = [3, 3, 1, 5 , 2]
    # Soumission des tâches au pool
    futures = [executor.submit(tache_longue, duree_arg) for duree_arg in durees_args]

    # Récupération des résultats
    for future in futures:
        print(future.result())