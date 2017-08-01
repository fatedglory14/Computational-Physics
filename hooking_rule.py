#Homework 7 Problem 5 Dimension of Symmetric Partition
#Andrew Turner

from numpy import *
from math import *

n = 4
sym_partition = [[1,1],[1,1]]
hooking_factor = 1

for i in range(len(sym_partition)):
    for j in sym_partition[i]:
        hook = sum(sym_partition[i][j:]) + sum(sym_partition[i:][j]) -1
        hooking_factor *= hook

dimension = factorial(n) / hooking_factor

print 'The dimension of the symmetric partition of %d is %d.' % (n, dimension)


'''If this code worked the algorithm would be as follows:
1: Assign a symmetric partition to an array of n by n filled with 1's.
2: Calculate the number of 1's below and to the right each index ij within the array.
3: Multiply each value for (2) to get the hooking factor.
4: For an integer n, calculate n! and divide by the hooking factor to get the dimension.

For this particular example, hooking factor should be (3*2*2*1), giving dimension = 2
'''
