s_suite="2;7;8;9;26;5"
values = s_suite.split(";")
for v in values :
    print(v)

values.insert(0,4)  #ajouter valeur 4 en position  0
values.append(30)
inverse_values=values.copy(); inverse_values.reverse()
print("values=",values)
print("values (ordre inverse)=",inverse_values)