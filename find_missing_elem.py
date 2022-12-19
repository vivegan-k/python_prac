import collections

def find_missing(l1, l2):
    d = collections.defaultdict(int)
    for i in l1:
        d[i] += 1

    for j in l2:
        d[j] -= 1

    for key in d.keys():
        if d[key] != 0:
            return key
print(find_missing([1,2,4,5,3,6], [1,2,4,5,3]))
