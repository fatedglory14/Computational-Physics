#Exercise 3.2 Evaluate a sum and write a test function
#Andrew Turner

def sum_1k(M):
    s = 0           #Sum
    k = 1           #Starting indice
    while k <= M:
        s += 1. / k
        k += 1
    return s

def test_sum_1k():     #Test function that calls sum_1k
    s = 11./6.
    exact = sum_1k(3)
    success = abs(exact - s) < 1E-14
    msg = '%s failed!' % (f.__name__)
    assert success, msg

print sum_1k(3)


