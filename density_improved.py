#Exercise 6.3 Use string operations to improve a program
#Andrew Turner

''' Original density.py file:'''

def read_densities(filename):
    infile = open(filename, 'r')
    densities = {}
    for line in infile:
        words = line.split()
        density = float(words[-1])

        if len(words[:-1]) == 2:
            substance = words[0] + ' ' + words[1]
        else:
            substance = words[0]

        densities[substance] = density
    infile.close()
    return densities

'''Part a: '''

def read_densities2(filename):
    infile = open(filename, 'r')
    densities = {}
    for line in infile:
        words = line.split()
        density = float(' '.join(words[-1:]))
        substance = ' '.join(words[:-1])
        densities[substance] = density
    infile.close()
    return densities

'''Part b: '''

def read_densities3(filename):
    infile = open(filename, 'r')
    densities = {}
    for line in infile:
        density = float(line[12:].strip())
        substance = line[:12].strip()
        densities[substance] = density
    infile.close()
    return densities

'''Part c: '''

filename = 'densities.dat'

def test_read_densities():
    if read_densities(filename) == read_densities2(filename) == read_densities3(filename):
        print 'All functions are equal.'
    else:
        print 'Failed.'

test_read_densities()


