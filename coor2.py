#Exercise 2.6 b Generate equally spaced coordinates (List comprehension)
#Andrew Turner

a = 0.               #Assign [a,b] and n.
b = 10.
n = 40

h = (b-a)/n          #Assign increment and starting position.

x = [a + i * h for i in range(0,n+1)]

for xval in x:
    print '%4.2f' % xval,
