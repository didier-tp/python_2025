import time

class MyTraceDump:

    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.f = open(self.filename,"wt")
        return self
    
    def dump(self,trace):
        self.f.write(f"{trace}\n")

    def __exit__(self, exc_type, exc_value, traceback):
        self.f.close()


class ChronoContext:
    def __enter__(self):
        self.debut = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.fin = time.time()
        self.duree = self.fin - self.debut
        print(f"elapsed time : {self.duree:.2f} s")

with ChronoContext() as chrono , MyTraceDump('my_traces.txt') as f_dump :
    # Bloc de code dont on souhaite mesurer le temps d'exécution via ChronoContext
    # et avec f_dump automatiquement ouvert et fermé:
    for i in range(10):
        time.sleep(0.1) # 0.1s de pause
        f_dump.dump(f"i={i}")