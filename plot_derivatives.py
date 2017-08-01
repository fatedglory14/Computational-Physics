#Homework 6 problem 5
#Andrew Turner

from math import *
from numpy import *
from matplotlib.pylab import *

#Define all functions and lists

h = [0.1, 0.01, 0.001, 1e-4, 1e-5, 1e-6]

def centerdiff(f, x, h):
    cdf = (f(x + h) - f(x - h)) / (2 * h)
    return cdf

def forwarddiff(f, x, h):
    fdf = (f(x + h) - f(x)) / h
    return fdf

f1 = lambda x: exp(-2*x**2)
f2 = lambda x: cos(x)
f3 = lambda x: sin(x)
df1 = lambda x: -4 * x * exp(-2*x**2)
df2 = lambda x: -sin(x)
df3 = lambda x: cos(x)

x1 = 2
x2 = 0.6
x3 = 0.6

exact1 = df1(x1)
exact2 = df2(x2)
exact3 = df3(x3)

centerapprox1 = []
centerapprox2 = []
centerapprox3 = []
forwardapprox1 = []
forwardapprox2 = []
forwardapprox3 = []
cerror1 = []
cerror2 = []
cerror3 = []
ferror1 = []
ferror2 = []
ferror3 = []

#Calculate Errors for each function

for step in h:
    step = float(step)
    centerapprox1.append(centerdiff(f1, x1, step))
    forwardapprox1.append(forwarddiff(f1, x1, step))
    centererror1 = abs(exact1 - centerapprox1)
    forwarderror1 = abs(exact1 - forwardapprox1)
    centerapprox2.append(centerdiff(f2, x2, step))
    forwardapprox2.append(forwarddiff(f2, x2, step))
    centererror2 = abs(exact2 - centerapprox2)
    forwarderror2 = abs(exact2 - forwardapprox2)
    centerapprox3.append(centerdiff(f3, x3, step))
    forwardapprox3.append(forwarddiff(f3, x3, step))
    centererror3 = abs(exact3 - centerapprox3)
    forwarderror3 = abs(exact3 - forwardapprox3)

#Make plots:

loglog(h[:-1],centererror1[:-1], label='Centered Err')
hold('on')
loglog(h[:-1],forwarderror1[:-1], label='Forward Err')
xlabel('h (step size)')
ylabel('Error')
legend()
title('Errors in derivative of exp(-2*x**2) at x=2')
show()

loglog(h[:-1],centererror2[:-1], label='Centered Err')
hold('on')
loglog(h[:-1],forwarderror2[:-1], label='Forward Err')
xlabel('h (step size)')
ylabel('Error')
legend()
title('Errors in derivative of cos(x) at x=0.6')
show()

loglog(h[:-1],centererror3[:-1], label='Centered Err')
hold('on')
loglog(h[:-1],forwarderror3[:-1], label='Forward Err')
xlabel('h (step size)')
ylabel('Error')
legend()
title('Errors in derivative of sin(x) at x=0.6')
show()


