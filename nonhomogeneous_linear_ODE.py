#Exercise C.1 Solve a nonhomogeneous linear ODE
#Andrew Turner

from math import *
from numpy import *
from matplotlib.pylab import *
from scitools.std import *

def ForwardEuler(f, U0, T, n):
    """Solve u'=f(u,t), u(0)=U0, with n steps until t=T."""
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
    return 2*u - 1

u, t = ForwardEuler(f, U0=2, T=6, n=24)
u_exact = .5 + 1.5*exp(2*t)
 
plot(t, u, 'r-', t, u_exact, 'b-',
     xlabel='t', ylabel='u', legend=('numerical', 'exact'),
     title="Solution of the ODE u'=2u-1, u(0)=2")


