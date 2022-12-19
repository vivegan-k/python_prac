from cgitb import reset
from collections import defaultdict
from unittest import result

def top_k_freq(li, k):
    d = {}

    for val in li:
        if val in d:
            d[val] += 1
        else:
            d[val] = 1
    values = list(d.values())
    li = []
    for i in range(k):
        max_val = max(values)
        li.append(max_val)
        values.remove(max_val)
    
    print(li)
    print(d)
    result = []
    for k, v in d.items():
        if d[k] in li:
            result.append(k)
    return result


print(top_k_freq([1,1,1,2,2,3,3,3,4], 2))
    
