phrase = input("phrase=")
print("phrase="+phrase)
mot=phrase.replace(' ',''); #supprimer tout les espaces:
print("mot phrase (sans espace)="+mot)
l = len(mot)
difference=False
for i in range(0,l//2+1):
    j=l-1-i
    c1=mot[i]; c2=mot[j]
    if c1!=c2 :
        print("pour i="+str(i) +" et j=" + str(j) + " c1=mot[i]=" + c1 +  " différent de c2=mot[j]="+c2)
        difference=True
        break

print("difference=",difference)
if difference :
    print(phrase+" n'est pas un palindrome")
else:
    print(phrase+" est un palindrome")