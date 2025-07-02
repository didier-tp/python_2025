with open("d5inputs.txt","rt") as finput :
    for ligneLue in finput :
        if ligneLue.endswith("\n") :
            ligneLue=ligneLue[:-1]
        print(ligneLue)
    #automatic call of .__exit__() et .close() à la fin du bloc with