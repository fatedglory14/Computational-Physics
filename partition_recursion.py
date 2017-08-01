#Problem 6 Homework 4
#Andrew Turner

import sys

nmax = int(raw_input('Enter number for nmax: '))
table = [0.0]*(nmax+1)

def append(terms, plusminus):
    table[plusminus] = terms

def p(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if table[n] != 0:
        return table[n]
    s = 0
    sign = 1
    for k in range(1, n+1):
        term_minus = n - k * (3 * k - 1) / 2
        if term_minus >= 0:
            term_1 = p(term_minus)
            append(term_1, term_minus)
        else:
            term_1 = 0 
        term_plus = n - k * (3 * k + 1) / 2
        if term_minus >= 0:
            term_2 = p(term_plus)
            append(term_1, term_plus)
        else:
            term_2 = 0
        term = term_1 + term_2 
        s = s + (sign*term)
        sign = -sign
    return s

n = 0
while n <= nmax:
    m = p(n)
    print n, m
    n += 1



#This doesn't work correctly, however, I feel like i'm closer than I was with the slow
#version that wasn't allowing me to get over n=30 in less than 30 minutes.




