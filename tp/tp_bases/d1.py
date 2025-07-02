import math
values= [ "81" , "-12" ,"36" , "abc" , "64" ]
for v in values:
    try:
        vn=int(v)  #vn=float(v)
        racine=math.sqrt(vn)
        print(f"vn={vn} racine={racine}")
    except Exception as e:
        print("une erreur a eu lieu:",e , type(e))