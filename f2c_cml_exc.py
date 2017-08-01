#Exercise 4.5
#Andrew Turner

import sys

try:
    F = float(sys.argv[1])
    C = (5. / 9) * (F - 32)
    print '%5.2f degrees Farenheit is %5.2f degrees Celsius.' % (F, C)
except IndexError:
    print 'C must be provided as command-line argument'
    sys.exit(1)
except ValueError:
    print 'C must be a number'
    sys.exit(1)
