#Exercise 5.1 Fill Lists with function values
#Andrew Turner

from math import *

def h(x):
    return 1 / sqrt(2 * pi) * exp(-0.5 * x**2.)

n = 41
dx = 8.0/(n-1)

xlist = [-4 + i*dx for i in range(n)]
hlist = [h(x) for x in xlist]
endlist = [[x, h] for x, h in zip(xlist, hlist)]

print 'X-Value    h(x)-Value'
for i in range(len(endlist)):
    print endlist[i]
