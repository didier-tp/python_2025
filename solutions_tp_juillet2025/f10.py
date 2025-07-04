import re
tab_val = [ "12.6" , "14,78" , "3.6" , "67,89", "1.4" , "124,677" , "134,67"]

def as_num_str(s):
    return re.sub(r",", "." , s)
    
def as_float(s):
    return float(as_num_str(s))    

tab_num_str=[as_num_str(s) for s in tab_val]
print("tab_num_str=",tab_num_str)

tab_float=[as_float(s) for s in tab_val]
print("tab_float=",tab_float)