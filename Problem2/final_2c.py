from cpt import *
from math import *
import numpy as np

V0 = 2
r0 = 2

def f (p) :
    r = p[0]
    #x = p[0]
    #y = p[1]
    #z = p[2]
    if (r>=0 and r<=4):
        return (sin(r-75.0)/(r-75.0))
    else :
        return 0
    #return x*x + 2 * y*y + 0.3 * cos(3 * pi * x) + 0.4 * cos(4 * pi * y) + sin(pi*z)

def negf (p) :
    r = p[0]
    #x = p[0]
    #y = p[1]
    #z = p[2]
    if (r>=74.0 and r<=76.0):
        return -(sin(r-75.0)/(r-75.0))
    else :
        return 0
 
    #return x*x + 2 * y*y + 0.3 * cos(3 * pi * x) + 0.4 * cos(4 * pi * y) + sin(pi*z)


def df(p) :
    l1 = p[0]
    r = ((cos(l1-75.0)/(l1-75.0))-(sin(l1-75.0)/((l1-75.0)*(l1-75.0))))
    return np.array( [r] )
    #l1 = p[0]
    #l2 = p[1]
    #l3 = p[2]
    #x = 2 * l1 - 0.9 * pi * sin(3 * pi * l1)
    #y = 4 * l2 - 1.6 * pi * sin(4 * pi * l2)
    #z = pi * cos(pi * l3)
    #return np.array( [x,y,z] )



p = input(" Enter starting point close to the maxima, i.e. 74.0: ")
#print p

k = float(p)
#print k
if (k<74.0 or k>76.0):
    k = 74.0

#print k
gtol = input( " Enter desired accuracy: ")
#print 'minimize'
#xmin = scipy.optimize.minimize( fun=f, x0=k, tol=gtol )
#fxmin = f(xmin.x)
#print xmin.x, fxmin

print 'maximize'
xmax = scipy.optimize.minimize( fun=negf, x0=k, tol=gtol )
fxmax = negf(xmax.x)
print 'The maxima is at = ', xmax.x
print 'The maximum value is = ', -fxmax
