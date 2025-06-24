import struct

listOfFloat=[]
for i in range(10):
    listOfFloat.append(float(i)+float(i)/100)

print("listOfFloat",listOfFloat)
#[0.0, 1.01, 2.02, 3.03, 4.04, 5.05, 6.06, 7.07, 8.08, 9.09]

structBinaryFormat="!d" # ! for network (big indian) , d for double/float

#ecriture de 10 "float/double" au format binaire dans le fichier data.bin
f=open("data.bin","wb")
for i in range(10):
    binary_float_value=struct.pack(structBinaryFormat,listOfFloat[i])
    #taille=len(binary_float_value) #size=8 for float as double
    #print(f"writing binary_float_value={binary_float_value} of size={taille}")
    f.write(binary_float_value)
f.close()

########################################################

#réouverture du fichier binaire data.bin
#et relecture d'une valeur sur 2
sublistOfFloat=[]
f2=open("data.bin","rb")
taille=8 # taille d'une valeur (ou enregistrement) binaire à lire
for i in range(10):
    if i%2==0:
        f2.seek(taille*i)
        binary_float_value = f2.read(taille)
        #print(f"read binary_float_value={binary_float_value}")
        float_valueTuple=struct.unpack(structBinaryFormat,binary_float_value)
        sublistOfFloat.append(float_valueTuple[0])
f2.close()
print("sublistOfFloat",sublistOfFloat)  #[0.0, 2.02, 4.04, 6.06, 8.08] 

'''
Points clefs:

* f.seek(position) permet de se positionner à une position bien précise
  au sein d'un fichier en accès direct/aléatoire de manière à préparer
  la prochaine lecture

* struct.pack(format,valeur(s)) permet de convertir 
  des valeurs python (str,int,float,...) en valeurs binaires (bytes)
  On peut convertit d'un seul coup un tableau entier de valeurs

* struct.unpack(format,valeur(s)) effectue la conversion inverse et renvoie
  un tuple de une ou plusieurs valeurs binaires converties en python
  
'''