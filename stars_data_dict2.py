#Exercise 6.6 Make a nested dictionary
#Andrew Turner

infile = open('stars.txt', 'r')
stars = {}    
print 'List of Stars to choose from:'
print
for line in infile.readlines()[1:-1]:
    data = line.split(',')
    N = data[0][2:-1]
    distance = float(data[-4])
    apparent_brightness = float(data[-3])
    luminosity = float(data[-2][:-1])
    stars[N] = {'distance': distance, 'apparent brightness': apparent_brightness, 'luminosity': luminosity}
    print N

print
name = raw_input('Enter the name of the star:')
print
print stars[name]
