
def myFunction(username="",password="",role=""):
    print(f'myFunction: username={username} password={password} role={role}')

myFunction()
myFunction("titi" , "pwd1" , "user")
myFunction(username="titi" , password="pwd1" ,role= "user")

myOrderedParamList=[  'tata',  'pwd2',  'admin']

myFunction(*myOrderedParamList) #unpack myOrderedParamList into ordered positional args of myFunction

myParamDict={
    'username' : 'toto',
    'password' : 'pwd3',
    'role' : 'admin'
}

myFunction(**myParamDict) #unpack myParamDict into kw-args of myFunction