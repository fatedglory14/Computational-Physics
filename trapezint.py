#Exercise 3.6: Integrate a function by the Trapezoidal rule
#Andrew Turner

from math import *
from scipy.integrate import quad

#Part a

print 'Parts A + B:\n'

def trapezint1(f, a, b):
    return (b-a) / 2. * (f(a) + f(b))

#Part b

f1 = (cos, 0, pi)
f2 = (sin, 0, pi)
f3 = (sin, 0, pi / 2)

functions = [f1, f2, f3]

def results(f, a, b):
    approx = trapezint1(f, a, b)
    exact = quad(f, a, b)[0]
    error = abs(exact - approx)
    print 'The exact value of the integral of %s from %d and %.3f is %.3f. \n The approximate value is %.3f which gives an error of %.3f' % (f.__name__, a, b, exact, approx, error)

for f in functions:
    results(f[0], f[1], f[2])

#Part c

print '\nPart C:\n'

def trapezint2(f, a, b):
    return (b-a) / 4. * (f(a) + 2 * f((a+b) / 2.) + f(b))

def results2(f, a, b):
    approx = trapezint2(f, a, b)
    exact = quad(f, a, b)[0]
    error = abs(exact - approx)
    print 'The exact value of the integral of %s from %d and %.3f is %.3f. \n The approximate value is %.3f which gives an error of %.3f' % (f.__name__, a, b, exact, approx, error)

for f in functions:
    results2(f[0], f[1], f[2])

#Part d

print '\nPart D:\n'

def trapezint(f, a, b, n):
    h = (b-a) / n
    x = (f(a) + f(b)) / 2
    for i in range(1, n):
        x += f(a + i * h)
    x *= h
    return x

def results3(f, a, b, n):
    approx = trapezint(f, a, b, n)
    exact = quad(f, a, b)[0]
    error = abs(exact - approx)
    print 'The exact value of the integral of %s from %d and %.3f is %.3f. \n The approximate value is %.3f which gives an error of %.3f' % (f.__name__, a, b, exact, approx, error)

for f in functions:
    results3(f[0], f[1], f[2], 10)

#Part e

tf1 = 0.000
tf2 = 1.984
tf3 = 0.998
test_functions = [tf1, tf2, tf3]


def test_trapezint():
    exact = trapezint(f, a, b, 1)
    success = abs(exact - test_functions) < 1E-14
    msg = '%s failed!' % (f.__name__)
    assert success, msg


