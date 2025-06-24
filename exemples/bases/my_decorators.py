def basic_decorateur(func):
    def wrapperFunction():
        print("> avant l'execution de la fonction originale")
        func()
        print("> après l'execution de la fonction originale")
    return wrapperFunction

def dire_bonjour():
    print("Bonjour !")

# Appliquer manuellement/explicitement le décorateur:
decoratedFunction = basic_decorateur(dire_bonjour)
decoratedFunction()

# Appliquer automatiquement le décorateur:
@basic_decorateur
def say_hello():
    print("Hello !")

say_hello()


def basic_decorateur2(func):
    def wrapperFunction(*args,**kwargs):
        print("> avant l'execution de la fonction avec args")
        res=func(*args,**kwargs)
        print("> après l'execution de la fonction avec args")
        return res
    return wrapperFunction

@basic_decorateur2
def say_hello_with_name(name):
    print(f"Hello {name} !")

say_hello_with_name("Laurence")

import time
def logExecutionTimeDeco(func):
    def wrapperFunction(*args,**kwargs):
        startTime=time.time()
        res=func(*args,**kwargs)
        endTime=time.time()
        print(f"Durée d'execution: {endTime - startTime:.4f} secondes")
        return res
    return wrapperFunction

@logExecutionTimeDeco
def calcul_lent(x):
    time.sleep(1)  # pause 1s pour simuler un calcul 
    print(f"calcul_lent({x}) returning {x*x}")
    return x*x

y=calcul_lent(5)
print("y=",y)


def logDecorator(func):
    def wrapperFunction(*args,**kwargs):
        print(f"*** Appel fonction {func.__name__} avec args={args} et kwargs={kwargs}")
        res=func(*args,**kwargs)
        print(f"*** valeur de retour = {res}")
        return res
    return wrapperFunction


'''
import logging

logging.basicConfig(level = logging.DEBUG)
logger = logging.getLogger()

def logDecorator(func):
    def wrapper(*args, **kwargs):
        funcName=func.__name__ # may display wrapper name rather than original name
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        logger.debug(f"function {funcName} called with args {signature}")
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            logger.exception(f"Exception raised in {funcName}. exception: {str(e)}")
            raise e
    return wrapper
'''

#will be applied: logDecorator(logExecutionTimeDeco(calcul_lent2(x)))
@logDecorator #outer decorator
@logExecutionTimeDeco #inner decorator
def calcul_lent2(x):
    time.sleep(1)  # pause 1s pour simuler un calcul 
    print(f"calcul_lent2({x}) returning {x*x}")
    return x*x

y=calcul_lent2(5)
print("y=",y)