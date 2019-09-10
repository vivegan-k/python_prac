# Example for dynamic array

import sys

n = 50
data = []

for i in range(n):
    print 'len of list: {0}; size of list: {1}'.format(len(data), sys.getsizeof(data))
    data.append(i)   
