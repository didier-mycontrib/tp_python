import math

def volumeSphere(rayon) :
    return 4/3 * math.pi * math.pow(rayon,3)

rayons = [ 5.0 , 10, 100]
for r in rayons :
    v = volumeSphere(r)
    print ("r=",r,"v=",v)