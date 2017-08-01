#Exercise 6.1 Make a dictionary from a table
#Andrew Turner


def read_constants(file):
    constants = {}
    infile = open(file, 'r')
    lines = infile.readlines()[2:]
    for line in lines:
        name = line[:27].strip()
        value = float(line[27:].split()[0])
        constants[name] = value
    infile.close()
    return constants

dict_constants = read_constants('constants.txt')

print '======================================='
print 'Constant Name:              Value:'
print '---------------------------------------'
for name, value in dict_constants.iteritems():
    print '%-27s %g' % (name, value)
print '---------------------------------------'




