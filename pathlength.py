#Exercise 3.12 Compute a pathlength
#Andrew Turner

from math import *

#Now we will define a test set of coordinates to read from

testcoord = [(1, 1), (1, 2), (1, 3), (1, 4)]  #Length should be 3 in this case.

#Next, read the coordinates into x and y for use.

x = [testcoord[i][0] for i in range(len(testcoord))]
y = [testcoord[i][1] for i in range(len(testcoord))]

#Now we can define our function for calculation of length.

def pathlength(x, y):
    L = 0.
    for i in range(1, len(x)):
        dlength = sqrt((x[i] - x[i - 1]) ** 2. + (y[i] - y[i - 1]) ** 2.)
        L += dlength
    return L

#Now we'll use a test function to ensure the program works correctly.

def test_pathlength():
    exact = 3.
    length = pathlength(x, y)
    success = abs(exact - length) < 1E-14
    msg = 'Program failed!'
    assert success, msg

print 'The length of the path is %.3f' % pathlength(x, y)
