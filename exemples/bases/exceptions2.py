def f1():
    excs = [OSError('erreur1'),SystemError('erreur2')]
    raise ExceptionGroup('plusieurs problemes', excs)

#f1()
'''
ExceptionGroup: plusieurs problemes (2 sub-exceptions)
  +-+---------------- 1 ----------------
    | OSError: erreur1
    +---------------- 2 ----------------
    | SystemError: erreur2
    +------------------------------------
'''

try:
    f1()
except Exception as e:
    print(f"exception rattrapée : {e} de type {type(e)}")


try:
    f1()
except* OSError as e:
    print(f"au moins une OsError a eu lieu dans ce sous groupe filtré {e}")
except* SystemError as e:
    print(f"au moins une SystemError a eu lieudans ce sous groupe filtré {e}")

def f2():
    raise TypeError('bad type')

#Enrichissement d'exception à retransmettre avec des notes
#ajoutées au niveau d'une fonction intermédiaire
#qui repropage d'exception :

def f3() :
    try:
        f2()
    except Exception as e :   
        e.add_note("f3 appelant f2 qui a planté")
        raise

#f3()
'''
TypeError: bad type
f3 appelant f2 qui a planté
'''    