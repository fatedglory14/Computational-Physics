#Exercise 6.2 Explore syntax differences
#Andrew Turner

#Consider the code:
t1 = {}
t1[0] = -5
t1[1] = 10.5

'''
t2 = []
t2[0] = -5
t2[1] = 10.5
'''

'''
Explain why t1 works fine but t2 does not:

t1 is a dictionary and 0 and 1 are keys that are assigned values.

t2 is a list, 0 and 1 are look up indices that are not found.
'''

'''
In order to correct the last code we must add 2 indices to the list:
'''

t2 = [0]*2
t2[0] = -5
t2[1] = 10.5
