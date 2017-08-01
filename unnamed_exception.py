#Exercise 4.18 Why we test for specific exception types
#Andrew Turner

#try:
#    C = float(sys.arg[1])
#except:
#    print 'C must be provided as command-line argument'
#    sys.exit(1)

########################################################
#Errors:

#1 NameError: name 'sys' is not defined.
# Add this next line. Also sys.arg is not defined, need sys.argv

#import sys

#try:
#    C = float(sys.arg[1])
#except:
#    print 'C must be provided as command-line argument'
#    sys.exit(1)

#2 C must be provided as command-line argument

# This is an index error, since there was only one argument
# provided the program exits due to the exception.

#To fix this problem we simply add another argument to the command-line
# i.e. >>python unnamed_exception argument

#import sys

#try:
#    C = float(sys.arg[1])
#except IndexError:
#    print 'C must be provided as command-line argument'
#    sys.exit(1)

#ValueError: could not convert string to float: a
# Now we get a value error, lets add an exception for that.

import sys

try:
    C = float(sys.argv[1])
except IndexError:
    print 'C must be provided as command-line argument'
    sys.exit(1)
except ValueError:
    print 'C must be a number'
    sys.exit(1)


