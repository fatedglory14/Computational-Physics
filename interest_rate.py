# Exercise 1.6 Compute the growth of money in a bank
# Andrew Turner

p = 5.0  # interest rate in percent
n = 3    # time in years
a = 1000 # intial deposit amount in euros

# Calculate the final amount using p and n

final = a*(1+(p/100))**n

print "After %g years, the amount is %.2f euros" % (n,final)
