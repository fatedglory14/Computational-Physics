#Exercise 2.16 Store data in a nested loop
#Andrew Turner

#part a

v0 = 15      # m/s
g = 9.8      # m/s**2
n = 20       # num of time intervals
dt = 2 * v0 / g / n

t = [i * dt for i in range(0,n+1)]
y = [v0 * t[i] - 0.5 * g * t[i] ** 2 for i in range(0,n+1)]

#Assign values for columns
ty1 = [t, y]

#Print header
print '%6s %6s' % ('t', 'y')
for i in range(len(t)):
    print '%6.2f %6.2f' % (ty1[0][i], ty1[1][i])

#part b

#Assign values for rows from ty1
ty2 = [[tval, yval] for tval, yval in zip(t, y)]

#Print header
print '%6s %6s' % ('t', 'y')
for tval, yval in ty2:
    print '%6.2f %6.2f' % (tval, yval)

