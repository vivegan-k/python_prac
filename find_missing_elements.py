import collections

def find_missing_elements(li1, li2):
    d = collections.defaultdict(int)
    for i in li2:
        d[i] += 1

    for i in li1:
        d[i] -=1

    for key in d:
        if d[key] != 0:
            return key

print find_missing_elements([1,2,4,5], [1,2,4,5,3])
