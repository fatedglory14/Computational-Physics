#Exercise 2.1 Make a Fahrenheit-Celsius conversion table
#Andrew Turner

print """\
------------------
%6s | %4s
------------------""" % ('F', 'C')  # table heading
F = 0                               # start value for F
dF = 10                             # increment of F in loop
while F <= 100:                     # loop heading with condition
    C = (5 / 9.) * (F - 32)         # formula for celsius
    print '%6.0f | %7.2f' % (F, C)    # print out value for F and C
    F += dF                         # reassign F
print '------------------'          # end of table line (after loop)
