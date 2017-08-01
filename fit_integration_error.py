#Exercise 2 Homework 8
#Andrew Turner

from numpy import *
from matplotlib.pyplot import *

f1= lambda x : x*2.
f2= lambda x : 3.*x**2
f3= lambda x : 4.*x**3

y1 = 4
y2 = 8
y3 = 16

def euler(y,f,x,dx,nsteps) :
    for i in range(nsteps) :
        y = y + f(x)*dx  # Euler algorithm 
        x += dx
    return x, y

x_0=1.
x_max=2.
y_0=1.
dx_list = [0.01**k for k in range(1,4)]
dx_print = 1.

y1errors = []
y2errors = []
y3errors = []

y=y_0; x=x_0

for dx in dx_list :
    nsteps = int(dx_print/dx)
    xf, yf = euler(y,f1,x,dx,nsteps)
    y1errors.append(abs(y1 - yf))
coeff = polyfit(dx_list, y1errors, 1)
y1fit = poly1d(coeff)
plot(dx_list, y1errors, '-')
xlabel('dx')
ylabel('Error')
title('Error vs. Step Size')
show()

for dx in dx_list :
    nsteps = int(dx_print/dx)
    xf, yf = euler(y,f2,x,dx,nsteps)
    y2errors.append(abs(y2 - yf))
coeff = polyfit(dx_list, y2errors, 2)
y2fit = poly1d(coeff)
plot(dx_list, y2errors, '-')
xlabel('dx')
ylabel('Error')
title('Error vs. Step Size')
show()

for dx in dx_list :
    nsteps = int(dx_print/dx)
    xf, yf = euler(y,f3,x,dx,nsteps)
    y3errors.append(abs(y3 - yf))
coeff = polyfit(dx_list, y3errors, 3)
y3fit = poly1d(coeff)
plot(dx_list, y3errors, '-')
xlabel('dx')
ylabel('Error')
title('Error vs. Step Size')
show()

print y1fit
print
print y2fit
print
print y3fit

'''Polynomials give:
1: 0.9998 dx + 2.02e-06
2: 11.62(dx**2) + 4.378 dx + 1.212e-05
3: 782.6(dx**3) + 21.42(dx**2) + 13.67 dx + 3.233e-05
'''




