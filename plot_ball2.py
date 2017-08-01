#Exercise 5.10: Plot a forumula for several parameters
#Andrew Turner

from numpy import *
from matplotlib.pylab import *
import sys

#Read in intial velocities

try:
    velocity = sys.argv[1:]
    if velocity == []:
        raise IndexError

#Exceptions

except IndexError:
    print 'Intial velocity must be provided as command-line argument'
    sys.exit(1)
except ValueError:
    print 'Intial velocity must be a number'
    sys.exit(1)

g = 9.81

for v0 in velocity:
    v0 = float(v0)
    t = linspace(0, 2*v0/g, 20)
    y = v0*t -0.5 * g * t**2.
    plot(t, y, label='Intial vel (m/s) = %g' % v0)

xlabel('time (s)')
ylabel('height (m)')
title('Height of ball in y-direction.')
legend()
show()


