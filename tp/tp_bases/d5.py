import math

with open("d5inputs.txt","rt") as finput , open("d5outputs.txt","wt") as foutput:
    for ligneLue in finput :
        try:
            if ligneLue.endswith("\n") :
                ligneLue=ligneLue[:-1]
            vn=int(ligneLue)
            racine=math.sqrt(vn)
            foutput.write(f"{racine}\n")
        except Exception as e:
            print("execption:",e)
    #automatic call of .__exit__() et .close() à la fin du bloc with

print("suite et fin de d5")    