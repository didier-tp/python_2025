age=33
ville='Rouen'
#message= j'ai 33 ans et j'habite Rouen
message='j\'ai {} ans et j\'habite {}'.format(age , ville)
print("message=",message)
message='j\'ai {1} ans et j\'habite {0}'.format(ville , age)
print("message=",message)
message='j\'ai {age} ans et j\'habite {ville}'.format(age=age , ville=ville)
print("message=",message)
