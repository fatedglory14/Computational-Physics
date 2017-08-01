#Exercise 3.8: Make an adaptive Trapezoidal rule
#Andrew Turner

from math import *
from scipy.integrate import quad

#First we need a function for calculating the 2nd derivative:

def df2(f, x, h=1E-6):
    fx = (f(x - h) - 2 * f(x) + f(x + h)) / (h ** 2.)
    return fx

#Second we need a function for evaluating the integral.

def trapezint(f, a, b, n):
    step = float((b-a) / n)
    tot = 0
    while (a < b):
        tot += 0.5 * step * (f(a) + f(a + step))
        a += step
    return tot

#Now we can calculate the value of n given eps:

def adaptive_trapezint(f, a, b, eps=1E-5):
    #First we need to set up the process of finding the max value of df2.
    num = 10000
    step = float((b-a) / num) #The value of the step needs to be a float.
    max_2df = 0
    #Now we can find the max value.
    max_2df = max(abs(df2(f, a+i*step)) for i in range(num+1))
    #With the max value we can now find h:
    h = sqrt(12 * eps) * 1 / sqrt((b-a)) * max_2df
    n = int((b - a) / h)
    print 'With n = %d' % n
    return trapezint(f, a, b, n)

f1 = (cos, 0, pi)
f2 = (sin, 0, pi)
f3 = (sin, 0, pi / 2)

functions = [f1, f2, f3]

def results(f, a, b):
    approx = adaptive_trapezint(f, a, b)
    exact = quad(f, a, b)[0]
    error = abs(exact - approx)
    print 'The exact value of the integral of %s from %d and %.8f is %.8f. \n The approximate value is %.8f which gives an error of %.8f\n' % (f.__name__, a, b, exact, approx, error)

for f in functions:
    results(f[0], f[1], f[2])

