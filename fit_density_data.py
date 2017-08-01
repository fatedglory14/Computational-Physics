#Exercise 5.17 Fit a polynomial to data points
#Andrew Turner

from numpy import *
from matplotlib.pyplot import *


def table(densityfile):
    data = {}
    data['Temp'], data['Density'] = loadtxt(densityfile, unpack=True)
    return data

def fit(x, y, deg):
    plot(x, y, 'o')
    coeff = polyfit(x, y, deg)
    yfit = poly1d(coeff)
    plot(x, yfit(x), '--')
    xmin = min(x) - ((max(x) - min(x))*0.05)
    xmax = max(x) + ((max(x) - min(x))*0.05)
    ymin = min(y) - ((max(y) - min(y))*0.05)
    ymax = max(y) + ((max(y) - min(y))*0.05)
    axis([xmin, xmax, ymin, ymax])
    xlabel('Temperature (C)')
    ylabel('Density at 1 atm (kg/m^3)')
    legend(['Values', 'Degree %d polynomial' % deg])
    title('Plot of Temperature vs. %s' % titlelabel)
    show()
#    print yfit

#Plot of air density

data = table('density_air.dat')
titlelabel = 'Density of Air'
fit(data['Temp'], data['Density'], 1)
fit(data['Temp'], data['Density'], 2)

# 1st Degree Poly:  -0.00442*x + 1.293
# 2nd Degree Poly:  1.411e-05*x^2 - 0.004702*x + 1.292

#Plot of water density

data = table('density_water.dat')
titlelabel = 'Density of Water'
fit(data['Temp'], data['Density'], 1)
fit(data['Temp'], data['Density'], 2)

#1st Degree Poly:  -0.4212*x + 1005
#2nd Degree Poly:  -0.003727*x^2 -0.04757*x + 1000


