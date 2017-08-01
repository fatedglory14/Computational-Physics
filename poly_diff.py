#Exercise 6.11 Compute the derivative of a polynomial
#Andrew Turner

def diff(p):
    diff_poly = {}
    for power, coeff in p.iteritems():
        if power != 0:
            diff_poly[power - 1] = power*coeff
    return diff_poly

p = {0: -3, 3: 2, 5: -1}
print diff(p)
