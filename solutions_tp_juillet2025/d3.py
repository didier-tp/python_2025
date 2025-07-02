import math

liste_taches=[
    { 'x': 81 , 'op': 'racine' , 'res' : '?' , 'status' :"todo" },
    { 'x': -81 , 'op': 'racine' , 'res' : '?' , 'status' :"todo"},
    { 'x': 6 , 'op': 'carre' , 'res' : '?' , 'status' :"todo"}
] 

def do_task(task):
    try:
        if task['op']=='carre':
            task['res']=math.pow(float(task['x']),2)
        elif task['op']=='racine':
            task['res']=math.sqrt(float(task['x']))
    except Exception as e:
        task['res']=e
    finally:
        task['status']="done"


for task in liste_taches:
    do_task(task)
for task in liste_taches:    
    print("task=",task)

def my_div(a,b):
    return a/b

def div_after_decrement(a,b):
    try:
        return my_div(a-1,b-1)
    except Exception as e:
        e.add_note(f"after division of {a}-1={a-1}  by {b}-1={b-1} ")
        raise# implicitly as raise e
      
       

res=div_after_decrement(9,5) # (9-1)/(5-1) = 8/4=2
print("(9-1)/(5-1) = 8/4=",res)


try:
    res2 = div_after_decrement(3,1) # (3-1)/(1-1) = 3/0 --> exception
    print("(3-1)/(1-1) = 3/0=",res2)
except Exception as err:
    print("(3-1)/(1-1) = 3/0=>exception =" ,err)
    try:
        print(err.__notes__)
    except:
        pass


