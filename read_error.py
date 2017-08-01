#Exercise 6.4 Interpret Output
#Andrew Turner

from numpy import *
from matplotlib.pyplot import *

infile = open('lnsum.dat', 'r')
lines = []

#Read relevant data into new list - lines

for line in infile:
    if line.find('epsilon') != -1:
        lines.append(line)
infile.close()

#Create dictionary for values:

data = {'epsilon': [], 'exact error': [], 'n': []}
for line in lines:
    information = line.split(',')
    data['epsilon'].append(float(information[0].split(':')[1]))
    data['exact error'].append(float(information[1].split(':')[1]))
    data['n'].append(float(information[2].split('=')[1]))

#Plot with log on y-axis using semilogy

semilogy(data['n'], data['exact error'])
xlabel('n')
ylabel('exact error')
show()
semilogy(data['n'], data['epsilon'])
xlabel('n')
ylabel('epsilon')
show()

