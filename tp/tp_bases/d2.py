def my_str_len(s):
    if isinstance(s,str): #verifier si s est de type str
        return len(s)
    else:
        #raise Exception("s pas de type str") #possible
        raise TypeError("s pas de type str mais de type" + str(type(s))) #mieux , plus précis
    
values = [ 5 , "abc" , "defgh" , 6.6]
for v in values:
    try:
        longueur=my_str_len(v) 
        print(f"pour v={v} longueur={longueur}")
    #except TypeError as te:
    #    print(f"une exception de type TypeError a eu lieu pour s={v}",te)        
    except Exception as e:
        #TypeError est vu comme un cas paerticulier de Exception (héritage)
        print(f"une exception a eu lieu pour s={v}",e)