#Exercise 5.3: Fill arrays; vectorized version
#Andrew Turner

from numpy import *

def h(x):
    return 1 / sqrt(2 * pi) * exp(-0.5 * x**2.)

xlist = linspace(-4, 4, 41)
hlist = h(xlist)

print 'X-Value    h(x)-Value'
for i in range(len(hlist)):
    print xlist[i], hlist[i]
