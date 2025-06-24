numbersAsStrings = [ "2" , "-1" , "45" , "6"]
numbers = [ int(sn) for sn in numbersAsStrings ]
print("numbers=",numbers) # [2, -1, 45, 6]

values = [ -1 , 3 , -6 , 7 ,-8 , 5 , -12 , 13]

positivesValues=[ v for v in values if v >=0 ]
print("positivesValues=",positivesValues) # [3, 7, 5, 13]

import math
values = [ -1 , 3 , -6 , 4 ,-8 , 5 , -12 , 2]
positivesValuesWithPowers=[ (v,v*v,math.pow(v,3)) for v in values if v >=0 ]
print("positivesValuesWithSquare=",positivesValuesWithPowers)
# [(3, 9, 27.0), (4, 16, 64.0), (5, 25, 125.0), (2, 4, 8.0)]


