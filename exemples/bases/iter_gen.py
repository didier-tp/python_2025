### itération basique avec fonction iter() et next() prédéfinies du langage python:
it = iter(range(3))
try:
    while True:
        print(next(it)) # affiche 0 puis 1 puis 2 puis provoque une exception StopIteration
except StopIteration:
        print("---fin iteration---")


### itérateur basique générant/renvoyant une par une
# les valeurs de startInclusive à stopExclusive:
class FromStartIncToStopExcIt:

    #constructor
    def __init__(self,startInc=0,stopExc=10):
        self.stopExc=stopExc # stop exclusive
        self.current = startInc - 1 # -1 : before first incrementation 

    # __iter(obj)__ return a iterator from a iterable object
    def __iter__(self):
        return self

    # __next()__ return next value until raise StopIteration
    def __next__(self):
        self.current += 1
        if self.current >= self.stopExc:
            raise StopIteration
        return self.current
    
for i in FromStartIncToStopExcIt(1,10):
    print(i)


### objet itérable renvoyant une par une
# les valeurs positives d'une collection après filtrage automatique:
class PositiveValuesFilterIterable :

    #constructor
    def __init__(self,col=[]):
        self.filteredCol=list(filter(lambda x : x>=0,col))

    # __iter(obj)__ return a iterator from this/self iterable object
    def __iter__(self):
        return iter(self.filteredCol)
        # pas besoin de __next__() ici car on retoure iter(...) comportant déjà __next()__

    
for v in PositiveValuesFilterIterable([1,-2,5,-6,8]):
    print("positive v=",v)

def my_basic_generator():
    yield "un"
    yield "deux"
    yield "trois"

for v in  my_basic_generator():
    print("generated value=",v)   

def fromStartIncToStopExcSquareTupleGenerator(startInc=0,stopExc=10):
    current = startInc
    while current < stopExc:
        yield (current,current * current)
        current +=1

for x_xx_tuple in fromStartIncToStopExcSquareTupleGenerator(0,10):
    print(x_xx_tuple)        