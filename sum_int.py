#Exercise 2.5 Sum of first n integers
#Andrew Turner

tot = 0             #Set intial sum
i = 1               #Set intial integer
n = 1000              #Set value for n

while i <= n:       #Condition
    tot += i        #Sum
    i += 1          #Reset integer value

print 'The sum of %2.0f integers is %2.0f' % (n, tot)

#Compared to the sum of n(n+1)/2

tot2 = 0
i = 1
n = 1000

while i <= n:
    tot2 = n*(n+1)/2
    i += 1

print 'The sum of n(n+1)/2 given %2.0f integers is %2.0f' % (n, tot2)


