#Problem 5 Homework 10
#Andrew Turner

from math import *
from numpy import *
from matplotlib.pylab import *
from scitools.std import *

#Forward Euler approximation:

def ForwardEuler(f, U0, T, n):
    t = np.zeros(n+1)
    u = np.zeros(n+1)  # u[k] is the solution at time t[k]
    u[0] = U0
    t[0] = 0
    dt = T/float(n)
    for k in range(n):
        t[k+1] = t[k] + dt
        u[k+1] = u[k] + dt*f(u[k], t[k])
    return u, t

# Problem: u'= 2u-1
def f(u, t):
    return 2*u-1

u, t = ForwardEuler(f, U0=2, T=6, n=24)
u_exact = .5 + 1.5*exp(2*t)
 
#Runge-Kutta 4th order:

def rk4(f, U0, T, n):
    rk_t = np.zeros(n+1)
    rk_u = np.zeros(n+1)  # u[k] is the solution at time t[k]
    rk_u[0] = U0
    rk_t[0] = 0
    dt = T/float(n)
    for k in range(n):
        rk_t[k+1] = rk_t[k] + dt
        k1 = dt*f(rk_u[k], rk_t[k])
        k2 = dt*f(rk_u[k] + dt/2., rk_t[k] + k1)
        k3 = dt*f(rk_u[k] + dt/2., rk_t[k] + k2)
        k4 = dt*f(rk_u[k] + dt, rk_t[k]+k3)
        rk_u[k+1] = rk_u[k] + k1/6. + k2/3. + k3/3. + k4/6.
    return rk_u, rk_t

rk_u, rk_t = rk4(f, U0=2, T=6, n=24)

#Error calculations:

rk_error = abs(rk_u - u_exact)
u_error = abs(u - u_exact)

semilogy(t, u_error, 'r-', t, rk_error, 'b-',
     xlabel='t', ylabel='error', legend=('Forward Error', 'RK4 Error'),
     title="Comparison of errors, EF vs. RK4")

