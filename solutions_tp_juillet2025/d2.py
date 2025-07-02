def my_str_len(s):
    s_type=type(s)
    if isinstance(s,str):
        return len(s)
    else:
        raise TypeError(f"s is not as string but {s_type}")


values = [ 5 , "abc" , "defgh" , 6.6]   
for v in values:
    try:
        print(f"v={v} my_str_len(v)={my_str_len(v)}")  
    except Exception as e:
        print(f"v={v} my_str_len(v) raise e of type={type(e)} with message={e}")  
