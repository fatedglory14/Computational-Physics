#Exercise 5.16: Plot data from a file
#Andrew Turner

from numpy import *
from matplotlib.pyplot import *
import sys

try:
    densityfile = sys.argv[1]
    legendlabel = str(sys.argv[1])

except IndexError:
    print 'Give the file name in the command line. Try again.'
    sys.exit(1)


def table(densityfile):
    infile = open(densityfile, 'r')
    data = {'Temp': [], 'Density': []}
    
    for line in infile:
        if line.isspace() or line.lstrip()[0] == '#':
            continue
        else:
            values = line.split()
            data['Temp'].append(float(values[0]))
            data['Density'].append(float(values[1]))
    
    data['Temp'] = array(data['Temp'])
    data['Density'] = array(data['Density'])
    
    infile.close()
    return data

def dataplot(x, y):
    plot(x, y, 'o')
    xmin = min(x) - ((max(x) - min(x))*0.05)
    xmax = max(x) + ((max(x) - min(x))*0.05)
    ymin = min(y) - ((max(y) - min(y))*0.05)
    ymax = max(y) + ((max(y) - min(y))*0.05)
    axis([xmin, xmax, ymin, ymax])
    xlabel('Temperature (C)')
    ylabel('Density at 1 atm (kg/m^3)')
    title('Plot of Temperature vs. %s' % legendlabel)
    show()

data = table(densityfile)
dataplot(data['Temp'], data['Density'])
