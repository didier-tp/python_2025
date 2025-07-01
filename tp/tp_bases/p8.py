def maxi_v1(a,b):
    res=0
    if a > b:
        res=a
    else:
        res=b
    return res

#appels: 
print("maxi 5,6: ",maxi_v1(5,6))
print("maxi 66,12: ",maxi_v1(66,12))   

#coder la fonction mini_v1
def mini_v1(a,b):
    res=0
    if a < b:
        res=a
    else:
        res=b
    return res
#appels: 
print("mini 5,6: ",mini_v1(5,6))
print("mini 66,12: ",mini_v1(66,12))