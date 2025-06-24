import sys
from my_util.op3 import tripleDe
#from my_util import tripleDe # ok que si my_util/__init__.py a d'office importer sous parties op3,op4

'''import p1.m1.aa
p1.m1.aa.aa1()'''

'''import p1.m1.aa as pm1a
pm1a.aa1()'''

'''from p1.m1.aa import aa1
aa1()'''

'''from p1.m1 import aa
aa.aa1()'''

from p1.m1 import * 
aa.aa1()

from p1.m2 import xx1
xx1()

def f1():
    print("f1")
    print(f"f1(), module_name: __name__ = {__name__}")  #valeur attendue=  __main__

#print("niveau principal d'execution du code python") 
#print(f"module_name: __name__ = {__name__}")  #valeur attendue=  __main__
#f1()
y=tripleDe(5)
print(f"y={y}")

#print("sys.path=",sys.path)
#print("dir(sys)=",dir(sys))
#print("dir()=",dir())

