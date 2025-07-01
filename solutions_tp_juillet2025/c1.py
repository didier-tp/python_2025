import math

def volume_sphere(rayon) :
    return 4/3 * math.pi * math.pow(rayon,3)

rayons = [ 5.0 , 10, 100]
for r in rayons :
    v = volume_sphere(r)
    print ("r=",r,"v=",v)