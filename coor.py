#Exercise 2.6 Generate equally spaced coordinates
#Andrew Turner

a = 0.               #Assign [a,b] and n.
b = 10.
n = 40

x = []               #Make an empty list.

h = (b-a)/n          #Assign increment and starting position.

for i in range(0,n+1):
    x.append(a + i * h)

for xval in x:
    print '%4.2f' % xval,
