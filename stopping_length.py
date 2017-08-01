#Exercise 4.15
#Andrew Turner

import sys

try:
    vo = float(sys.argv[1]) # km/hr
    mu = float(sys.argv[2]) # dimensionless
    g = 9.81                # m/s**2

    #Convert vo to m/s

    vconvert = (1000./3600)*vo

    #Calculate distance

    d = (0.5 * ((vconvert**2) / (mu * g))) # meters

    print 'Given an intial velocity of %5.2f km/hr, and friction coefficient %5.2f,\n the braking distance needed is %5.2f meters.' % (vo, mu, d)

except IndexError:
    print 'Intial velocity and friction coefficient must be \nprovided as command-line arguments.'
    sys.exit(1)
    sys.exit(2)
except ValueError:
    print 'Intial velocity and friction coefficient must be numbers.'
    sys.exit(1)
    sys.exit(2)
