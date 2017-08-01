#Exercise 3 Homework 8
#Andrew Turner

from math import *

'''In this code I used previous coding provided by the professor'''

def transpose_partition(p):
    longest_height=len(p)
    column_height = [longest_height]*p[-1]	# there are p[-1] columns with the maximum height
    length_of_prior_row = p[-1]
    ind = -2	# ind is index from end of partition p
    while ind >= -len(p) :
        if p[ind] > length_of_prior_row :   # add more columns
            current_height = len(p) +1 + ind
            column_height += [current_height] * (p[ind]-length_of_prior_row)
	    length_of_prior_row = p[ind]
	ind -= 1
    return column_height

def hooking_rule(p):
    column_heights = transpose_partition(p)
    prod = 1
    #  iterate over each box in partition p
    for row in range(len(p)) :
        for column in range(p[row]) :
	    hook = (p[row] - column) + (column_heights[column] - row) -1
	    prod *= hook
	    #print row,column,hook
    return factorial(sum(p))/prod

def makepartitions(n):
    partitionlist=[ [[1]] ]
    ncurrent = 1    # current completed value of n
    while ncurrent < n:
        ncurrent += 1
        nparts=[]  # nparts is the list partitions of ncurrent
        nparts.append([ncurrent])   # first new partition of ncurrent
        nmax = ncurrent - 1
        while nmax > 0:
            firstrow = [nmax]   # need to add partitions of ncurrent - nmax
            rest = ncurrent - nmax
            partitions = partitionlist[rest -1]   # partitions of rest
            for i in partitions:
                if i[0] <= nmax:
                    newpartition = firstrow + i
                    nparts.append( newpartition )
            nmax -= 1
        partitionlist.append(nparts)
    return nparts

n_list = [k for k in range(2,11)]

# Special case for n = 1

print 'The partitions of n = 1 are:'
print '[[1]]'
print '\nThe outputs of the hooking rule are:'
print [1]
print '\nThe sum over p of d(p**2): 1'
print 'Compare this to 1 factorial: 1\n\n'

#For partitions n = 2 - 10

for n in n_list:
    nparts = makepartitions(n)
    print 'The partitions of n = %d are:' % n
    print nparts
    d = []
    d2 = []
    for i in nparts:
        d.append(hooking_rule(i))
        d2.append(hooking_rule(i)**2)
    print '\nThe outputs of the hooking rule are:'
    print d
    print '\nThe sum over p of d(p**2): %d' % sum(d2)
    print 'Compare this to %d factorial: %d\n\n' % (n, factorial(n))    
