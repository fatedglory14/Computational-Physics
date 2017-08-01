#Exercise 2.19 Explore what zero can be on a computer
#Andrew Turner

eps = 1.0
while 1.0 !=1.0 + eps:
    print '...............', eps
    eps = eps/2.0
print 'final eps:', eps

#This program attempts to find 0 to the point that
#1.0 + eps is equal to 1.0.  The value of eps at the
#end of the loop is what the computer considers
#as close enough to zero.  Each iteration allows eps
#to tend closer and closer to zero until the computer
#cannot tell the difference.  This value is printed at
#the end of the program.
