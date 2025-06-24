print(1 + 2) # addition → 3
print("debut_"+"suite")  # concatenate two strings →  debut_suite

print(3 * 4) # Product two numbers → 12
print("Abc"*4) # Repeat the  string → "AbcAbcAbcAbc"

class MyBasicArray:
    #constructor:
    def __init__(self,*args):
        self.values = list(args)

    def __str__(self):
        sA="["
        for a in self.values:
            sA += ( str(a)+ ",")
        return sA[:-1] + "]"

    # adding two arrays (self and other)
    def __add__(self, other):
        resArray= MyBasicArray()
        for i in range(len(self.values)):
            v1=self.values[i]
            v2=other.values[i]
            resArray.values.append(v1+v2)
        return resArray
    
a1 = MyBasicArray(2,4,8); print("a1",a1) # [2,4,8]
a2 = MyBasicArray(6,1,7); print("a2",a2) # [6,1,7]
a3=a1+a2 # operator + between two instances of MyBasicArray ( __add__(self,other) )
print("a3=a1+a2=",a3) #[8,5,15]
