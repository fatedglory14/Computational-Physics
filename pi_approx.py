#Exercise 3.13 Approximate pi
#Andrew Turner

from math import *

#First call the path length function from before

def pathlength(x, y):
    L = 0.
    for i in range(1, len(x)):
        dlength = sqrt((x[i] - x[i - 1]) ** 2. + (y[i] - y[i - 1]) ** 2.)
        L += dlength
    return L

#Now we can define a function for the points through n

def coord(n):
    x = [0.5 * cos(2*pi*i / n) for i in range(n+1)]
    y = [0.5 * sin(2*pi*i / n) for i in range(n+1)]
    return x, y

num = [2 ** k for k in range (2, 11)]

for n in num:
    x, y = coord(n)
    piapprox = pathlength(x, y)
    print 'Number of points: %4d  Pi Approximate: %.8f Error: %.8f' % (n, piapprox, abs(pi - piapprox))
