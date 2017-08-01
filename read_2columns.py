#Exercise 5.14 Plot data in a two-column file
#Andrew Turner

from numpy import *

x = []
y = []

infile = open('xy.dat', 'r')
for line in infile:
    xylist = line.split()
    x.append(float(xylist[0]))
    y.append(float(xylist[1]))
infile.close()

x = array(x)
y = array(y)

ymin = min(y)
ymax = max(y)
ymean = mean(y)

xmin = x.min()
xmax = x.max()
xmean = x.mean()

print 'y-minimum = %f' % ymin
print 'y-maximum = %f' % ymax
print 'y-mean    = %f' % ymean

#print 'x-minimum = %f' % xmin
#print 'x-maximum = %f' % xmax
#print 'x-mean    = %f' % xmean

