import math

with open("d5inputs.txt","rt") as fi , open("d5outputs.txt","wt") as fo:
    ligneLue="?"
    while ligneLue:
        ligneLue=fi.readline()
        if ligneLue.endswith("\n") :
            ligneLue=ligneLue[:-1]  # enlever le dernier caractère
        if len(ligneLue)>0:
            val=float(ligneLue)
            racine = math.sqrt(val)
            fo.write(f"{racine}\n")