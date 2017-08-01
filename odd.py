#Exercise 2.4 Generate odd numbers
#Andrew Turner

#Define the ending value n, and starting value p.

n = 36
p = 0

#Start loop to check if number is odd then print

while p < int(round(n/2.)):

#If true then print the odd number it represents

    print 2 * p + 1,

#Continue with the next integer...

    p = p + 1
