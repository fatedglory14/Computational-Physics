#Exercise 6.7 Make a nested dictionary from a file
#Andrew Turner

#Open file and sort lines into appropriate places.

infile = open('human_evolution.txt', 'r')
lines = infile.readlines()
data = []
header = lines[0:3]
footer = lines[10:13]
for line in lines:
    if line.find('H.') != -1:
        data.append(line)
infile.close()

#Create dictionary

humans = {}
for line in data:
    species = line[:21].strip()
    when = line[21:37].strip()
    height = line[37:50].strip()
    mass = line[50:62].strip()
    brain_volume = line[62:].strip()
    humans[species] = {'when': when,
                                    'height': height,
                                    'mass': mass,
                                    'brain volume': brain_volume}

#Output

print header[2],header[0],header[1],header[2]
for species in humans:
    print '%-20s %-15s %-12s %-11s %-22s' % (species,
                                             humans[species]['when'],
                                             humans[species]['height'],
                                             humans[species]['mass'],
                                             humans[species]['brain volume'])
print footer[0],footer[1],footer[2]

