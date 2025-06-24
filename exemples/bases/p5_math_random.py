#from math import *
#---> pi , e , sin() , sqrt() , ...

import math;
# ---> math.pi , math.e , math.sin() , math.sqrt() , ...

#NB: sqrt() calcule la racine carree (square root).

#resolution ax^2+bx+c=0
def resol_eq_2nd_degre(a,b,c):
	delta = b*b-4*a*c
	if delta==0 :
		x1=x2=-b/(2*a)
	if delta > 0:
		x1=(-b-math.sqrt(delta))/(2*a)
		x2=(-b+math.sqrt(delta))/(2*a)
	if delta <0:
		x1=(-b-1j*math.sqrt(-delta))/(2*a)
		x2=(-b+1j*math.sqrt(-delta))/(2*a)
	print("solutions pour equation ax^2+bx+c=0 avec a=",a, "b=",b , "c=" ,c );
	print("x1=",x1)
	print("x2=",x2)
		
resol_eq_2nd_degre(2,-9,-5); # x1=-0.5 et x2=5

resol_eq_2nd_degre(2,-1,-6); # x1=-1.5 et x2=2

resol_eq_2nd_degre(1,3,9/8); # x1=x2=4/4=0.75

resol_eq_2nd_degre(1,2,5); # x1=-1-2j et -1+2j avec j=i et j^2=i^2=-1

###############################"

print("pi=",math.pi) # 3.141592653589793
print("e=",math.e) # 2.718281828459045
print("sin(pi/6)",math.sin(math.pi/6)) # 0.49999999999999
y=math.pow(2,3); print("2 puissance 3 = " , y); # 8

#################################

import random 

x =random.random()        # Random float x, 0.0 <= x < 1.0
print(x) # x=0.3581652418510137 ou autre

x=random.uniform(1, 10)  # Random float x, 1.0 <= x < 10.0
print(x) # x=6.1800146073117523 ou autre

x=random.randint(1, 10)  # Integer from 1 to 10, endpoints included
print(x) # x=6 ou autre

import string
small_letters = string.ascii_lowercase # séquence des caractères de a à z
print(small_letters)
c=random.choice( small_letters) # retourne un éléments de la séquence
                                # choisi aléatoirement : ici une lettre en a et z
print(c) # affiche c ou r ou autre

sub_list = random.sample([1, 2, 3, 4, 5],  3)  # Choose 3 elements
print(sub_list) # affiche [5, 2, 1] ou autre
