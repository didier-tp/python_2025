def addition(a,b,comment,d):
    #print(f"lors de l'appel a={a} , b={b} comment={comment}")
    somme=a+b
    comment=comment+"*"
    d["somme"]=somme; d["a"]=a; d["b"]=b
    print(f"lors fin appel a={a} , b={b} comment={comment}")
    return somme

c="add"
dico=dict({})
s1=addition(3,4,c,dico); 
print("s1=",s1, "c=" , c , "dico=",dico)

x=5; y=9
s2=addition(x,y,"add",dico); print("s2=",s2 , "dico=",dico)

'''
En python:
   int,float,str,tuple,byte,bool : immutable (non modifiable)
   ----
   Autres choses: list,set,dict,objets : modifiable
'''

#########################""

def calculer_puissance(x,n):
    produit=1
    i=0
    while i<n:
        i+=1
        produit = produit *x
    return produit

def calculer_puissance_recursive(x,n):
    if n==0 :
        return 1
    else:
        return x * calculer_puissance_recursive(x,n-1)

p1= calculer_puissance(2,3); print("p1=",p1)
p2= calculer_puissance_recursive(2,3); print("p2=",p2)