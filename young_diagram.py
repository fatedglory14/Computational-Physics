#Homework 7 Problem 4 Plot Young Diagram of Partition
#Andrew Turner

from numpy import *
from matplotlib.pyplot import *
from matplotlib.patches import *
from matplotlib.collections import PatchCollection

#Calculate the partition of n

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

def transpose_partition(p):
    column_height = [0*p]	# there are p[0] columns
    column_height = array(column_height)
    for i in p:
        j=0
        while j < i:
            column_height[j] += 1
            j += 1
    return column_height

nparts = makepartitions(4)
nparts = array(nparts)
cheights = []

cheights.append([transpose_partition(nparts[i]) for i in nparts])  #Height of each column in nparts

print nparts, cheights

'''If my code worked this would be the algorithm:
1: Calculate partitions of integer n
2: For each partition of n find the maximum height of each column
3: For max column height in each partition plot horizontal lines for range(0, max(cheights[i]))
4: Define a range for each horizontal line depending on the length of each row in the partition.
5: Plot verticle lines for each row depending on length of each row.
6: Show plots for each partition of n.'''

        
    
    

