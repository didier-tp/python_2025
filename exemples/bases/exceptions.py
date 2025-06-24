def my_division(x,y):
	if y==0 :
		raise Exception("division par zéro invalide")
	else :
		return x/y
		
a=6
#b=2
b=0

try :
	c=my_division(a,b);
	print("res my_division=" , c)
except Exception as e :
    print("une erreur a eu lieu :" , e)


try :
	c=a/b
	print("res division=" , c)
except :
	print("attention: une erreur s'est produite !!!")
	
print("suite du programme qui ne s'est pas planté")
  




