#Exercise 3.18 Write a function for numerical differentiation
#Andrew Turner

from math import *

#Part a

def diff(f, x, h=1E-5):
    df = (f(x + h) - f(x - h)) / (2 * float(h))
    return df

#Part b

#Define a test f(x)

def test(x):
    ftest = x**2 + x + 1
    return ftest

def test_diff():
    exact = 3. 
    answer = diff(test, 1)
    success = abs(exact - answer) < 1E-14
    msg = 'Program failed!'
    assert success, msg

#print diff(test, 1)    #Line for debugging.

#Part c

#Apply diff to the functions for h = 0.01 and collect in application function

f1 = lambda x: exp(x)                     #Define functions and derivatives.
f2 = lambda x: exp(-2*x**2)
f3 = lambda x: cos(x)
f4 = lambda x: log(x)
df1 = lambda x: exp(x)
df2 = lambda x: -4 * x * exp(-2*x**2)
df3 = lambda x: -sin(x)
df4 = lambda x: 1 / x

functions = [f1, f2, f3, f4]              #Put these into their retrospective lists.
dfunctions = [df1, df2, df3, df4]
xvalues = [0, 0, 2*pi, 1]
fname = ['exp(x)', 'exp(-2x**2)', 'cos(x)', 'ln(x)']

#Header for list of values.

print '%s %5s %9s %9s %7s' % ('Function', 'X', 'Exact', 'Approx', 'Error')

#Application function

def application():
    applist = []
    for name, f, df, x, in zip(fname, functions, dfunctions, xvalues):
        exact = df(x)
        approx = diff(f, x, h=0.01)
        error = abs(exact - approx)
        print '%12s %.3f %.6f %.6f %.6f' % (name, x, exact, approx, error)
        applist.append(error)
    print
    print 'List of errors:'
    print applist
    return applist
    
#Call the function

application()

    
