import random as r
import math

MAX_POINTS = 2**30

def getPoint():
    """
        A Point as (x,y)
    """
    return (r.random(), r.random())


def isInCircle(p):
    x,y = p[0], p[1]
    if ((x**2 + y**2) <= 1):
        return True
    return False


if __name__ == "__main__":
    count = 0
    for i in range(0, MAX_POINTS):
        p = getPoint()
        if (isInCircle(p)):
            count += 1
    
    roughPi = (4.0 * (1.0 * count)/ (1.0 * MAX_POINTS) )
    
    print("Value of Pi is roughly %1.6f" % roughPi )
    print("Error of %0.3f %%" % ((math.pi - roughPi)/math.pi))
    
        