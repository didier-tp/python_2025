def ma_factorielle(n): 
    res=1
    for i in range(1,n+1):
        res= res * i
    return res

def ma_factorielle_recursive(n): 
    if n==0:
        return 1
    else:
        return n * ma_factorielle_recursive(n-1)

values=[0,1,2,3,4,5,6,7]
for n in values:
    f = ma_factorielle(n)
    f2 = ma_factorielle_recursive(n)
    print(f"n={n} n!={f}={f2}")