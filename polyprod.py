#Exercise 3.5: Compute a polynomial via a product
#Andrew Turner

#Test list of roots
roots = [2, 3, 4, 5]

def poly(x, roots):
    p = 1		#Starting value for p(x)
    for i in range(len(roots)):
        p *= (x - roots[i])
    return p

print 'The product of the %d roots, %s, given x=1 is: %d' % (len(roots), roots, poly(1,roots))
