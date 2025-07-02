f= open("my_fic.txt","rt")
ligneLue="?"
while ligneLue :
	ligneLue=f.readline() 
	if ligneLue.endswith("\n") :
		ligneLue=ligneLue[:-1]  # enlever le dernier caractère
	if len(ligneLue)>0 :
		print(f"**{ligneLue}**")
f.close()