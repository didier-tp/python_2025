import math
values= [ "81" , "-12" ,"36" ,  "abc" , "64" ]
for v_str in values:
    try:
        val_num = float(v_str)
        racine = math.sqrt(val_num)
        print(f"val_num={val_num} racine={racine}")
    except Exception as e:
        print("for v_str=",v_str," e=",e , " of type=", type(e))