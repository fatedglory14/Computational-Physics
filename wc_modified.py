#Problem 5
#Andrew Turner

import sys

totline = 0
totbytes = 0
totwordcount = 0

for i in sys.argv[1:]:
    A = i
    lines = 0
    wordcount = 0
    bytes = 0
    infile = open(A, 'r')
    for line in infile:
        lines += 1
        bytes += len(line)
        wordcount += len( line.split())
    totline += lines
    totbytes += bytes
    totwordcount += wordcount 
    print '%4d %4d %4d %s' % (lines, bytes, wordcount, A)
print '%4d %4d %4d total' % (totline, totbytes, totwordcount)
