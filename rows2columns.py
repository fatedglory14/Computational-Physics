#Question 6 Homework 3
#Andrew Turner

#Create an array to analyze

test = ([[1], [2, 3], [3, 4, 5], [6, 7, 8, 9]])

ncurrent = 1
n = 0
rowstocolumns = []
col1 = []
col2 = []
col3 = []
col4 = []
#Rewrite the list into a new list of columns:
while ncurrent <= len(test):
    while ncurrent == 1:
        for i1 in range(len(test)):
            position = test[i1][0]
            col1.append(position)
        rowstocolumns.append(col1)
        print 'Column 1 has height: %d' % (len(col1))
        ncurrent += 1
    while ncurrent == 2:
        for i2 in range(1, len(test)):
            position = test[i2][1]
            col2.append(position)
        rowstocolumns.append(col2)
        print 'Column 2 has height: %d' % (len(col2))
        ncurrent += 1
    while ncurrent == 3:
        for i3 in range(2, len(test)):
            position = test[i3][2]
            col3.append(position)
        rowstocolumns.append(col3)
        print 'Column 3 has height: %d' % (len(col3))
        ncurrent += 1
    while ncurrent == 4:
        for i4 in range(3, len(test)):
            position = test[i4][3]
            col4.append(position)
        rowstocolumns.append(col4)
        print 'Column 4 has height: %d' % (len(col4))
        ncurrent += 1
    ncurrent += 1
print rowstocolumns

# I am sure there is something i'm missing to make this more elegant.

