#Exercise 5.4: Make a plot
#Andrew Turner

from numpy import *
from matplotlib.pylab import *

def h(x):
    return 1 / sqrt(2 * pi) * exp(-0.5 * x**2.)

xlist = linspace(-4, 4, 41)
hlist = h(xlist)

plot(xlist, hlist)
xlabel('X-Value')
ylabel('h(x)-Value')
legend(['1/sqrt(2*pi) * exp(-0.5 * x**2.)'])
axis([-4, 4, 0, 0.4]) # [xmin, xmax, ymin, ymax]
title('Exercise 5.4: Make a plot')
show()
