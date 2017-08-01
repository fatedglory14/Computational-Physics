#Exercise 4.1
#Andrew Turner

try:
    F = float(raw_input('Input degrees in Farenheit: '))
    C = (5. / 9) * (F - 32)
    print '%5.2f degrees Farenheit is %5.2f degrees Celsius.' % (F, C)
except ValueError:
    print 'C must be a number, try again.'
