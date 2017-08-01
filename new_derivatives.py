#Exercise 1 Homework 8
#Andrew Turner

from math import *
from numpy import *
from matplotlib.pylab import *

'''Part a:

RECALL: forward difference : ( f(x+h) - f(x) ) / h
--> Leading error is order h.
--> D(h) = A + epsilon * h
--> D(2h) = A + epsilon * 2h
--> 2*D(h) = 2A + 2epsilon * 2h
--> 2*D(h) - D(2h) = 2A - A + 2epsilon*h - 2epsilon*h
--> 2*D(h) - D(2h) = A

Central Difference : ( f(x+h)-f(x-h) ) / (2. * h)
--> Leading error is order h**2
--> D(h) = A + epsilon * h**2
--> D(2h) = A + epsilon * 4*h**2
--> 4*D(h) = 4A + epsilon * 4*h**2
--> 4*D(h) - D(2h) = 4A - A + 4epsilon*h**2 - 4epsilon*h**2
--> (4*D(h) - D(2h)) / 3 = A
'''

'''Part b:'''

def extrap_fdiff(f, x, h):
    fdiff1 = (f(x + h) - f(x)) / h
    fdiff2 = (f(x + 2*h) - f(x)) / (2.*h)
    fdiff = 2*fdiff1 - fdiff2
    return fdiff

def extrap_cdiff(f, x, h):
    cdiff1 = (f(x + h) - f(x - h)) / (2 * h)
    cdiff2 = (f(x + 2*h) - f(x - 2*h)) / (4. * h)
    cdiff = (4*cdiff1 - cdiff2) / 3.
    return cdiff

'''Part c:'''

f1 = lambda x: exp(x)                     #Define functions and derivatives.
f2 = lambda x: exp(-2*x**2)
f3 = lambda x: cos(x)
f4 = lambda x: log(x)
df1 = lambda x: exp(x)
df2 = lambda x: -4 * x * exp(-2*x**2)
df3 = lambda x: -sin(x)
df4 = lambda x: 1 / x
x1 = 0
x2 = 0
x3 = 2*pi
x4 = 1.
exact1 = df1(x1)
exact2 = df2(x2)
exact3 = df3(x3)
exact4 = df4(x4)

centerapprox1 = []
centerapprox2 = []
centerapprox3 = []
centerapprox4 = []
forwardapprox1 = []
forwardapprox2 = []
forwardapprox3 = []
forwardapprox4 = []
centererror1 = []
centererror2 = []
centererror3 = []
centererror4 = []
forwarderror1 = []
forwarderror2 = []
forwarderror3 = []
forwarderror4 = []

hvals = [0.1**k for k in range(1,6)]

for step in hvals:
    centerapprox1 = extrap_cdiff(f1, x1, step)
    forwardapprox1 = extrap_fdiff(f1, x1, step)
    centererror1.append(abs(exact1 - centerapprox1))
    forwarderror1.append(abs(exact1 - forwardapprox1))
    centerapprox2 = extrap_cdiff(f2, x2, step)
    forwardapprox2 = extrap_fdiff(f2, x2, step)
    centererror2.append(abs(exact2 - centerapprox2))
    forwarderror2.append(abs(exact2 - forwardapprox2))
    centerapprox3 = extrap_cdiff(f3, x3, step)
    forwardapprox3 = extrap_fdiff(f3, x3, step)
    centererror3.append(abs(exact3 - centerapprox3))
    forwarderror3.append(abs(exact3 - forwardapprox3))
    centerapprox4 = extrap_cdiff(f4, x4, step)
    forwardapprox4 = extrap_fdiff(f4, x4, step)
    centererror4.append(abs(exact4 - centerapprox4))
    forwarderror4.append(abs(exact4 - forwardapprox4))

'''Part d:'''

#Make plots:

loglog(hvals[:-1],centererror1[:-1], label='Centered Err')
hold('on')
loglog(hvals[:-1],forwarderror1[:-1], label='Forward Err')
xlabel('h (step size)')
ylabel('Error')
legend()
title('Errors in derivative of exp(x) at x=0')
show()

#This function is plotted normally because of values ~ 0.

plot(hvals[:-1],centererror2[:-1], label='Centered Err')
hold('on')
plot(hvals[:-1],forwarderror2[:-1], label='Forward Err')
xlabel('h (step size)')
ylabel('Error')
legend()
title('Errors in derivative of exp(-2*x**2) at x=0')
show()


loglog(hvals[:-1],centererror3[:-1], label='Centered Err')
hold('on')
loglog(hvals[:-1],forwarderror3[:-1], label='Forward Err')
xlabel('h (step size)')
ylabel('Error')
legend()
title('Errors in derivative of cos(x) at x=2*pi')
show()

loglog(hvals[:-1],centererror4[:-1], label='Centered Err')
hold('on')
loglog(hvals[:-1],forwarderror4[:-1], label='Forward Err')
xlabel('h (step size)')
ylabel('Error')
legend()
title('Errors in derivative of log(x) at x=1')
show()

'''
Since the error is still growing as a function of h (much slower than before),
we must look at the second error term in the taylor expansion of the functions.

For the first function this error goes as h**2

For the second function this error goes as h**4

'''
