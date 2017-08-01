#Exercise 4.4 Read and write several from and to a file
#Andrew Turner

def write_data(outfile):
    outfile = open(outfile, 'w')
    infile = open('Fdeg.dat', 'r')
    infile.readline()               #Skip first 2 lines.
    infile.readline()
    F = []
    for line in infile:
        table = line.split()        #Three columns in this table, only need [2]
        F = float(table[2])
        celsius = (5. / 9) * (F - 32)
        outfile.write('%5.2f degrees F is %.2f degrees C\n' % (F, celsius)) 
    infile.close()
    outfile.close() 

write_data('Cdeg.dat')
