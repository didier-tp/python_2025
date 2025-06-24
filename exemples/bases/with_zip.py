keys=["red","green","blue"]
values=["rouge","vert","bleu","black"]
col3=['un','deux','trois','quatre']
#zipObject_as_iteratorOnTuple = zip(keys,values)
#colorDict = dict(zipObject_as_iteratorOnTuple)
colorDict = dict(zip(keys,values))
print("colorDict=" + str(colorDict))

experimentalTupleList = list(zip(keys,values,col3))
print("experimentalTupleList=" + str(experimentalTupleList))

#colorDict2 = {keys[i] : values[i] for i, v in enumerate(keys)}
colorDict2 = {keys[i] : values[i] for i, _ in enumerate(keys)}  # _ is for unused special variable name
print("colorDict2=" + str(colorDict2))