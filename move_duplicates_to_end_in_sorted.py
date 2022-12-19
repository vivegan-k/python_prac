li = '1 1 1 1 2 2 3 4 5 5'.split()

def move_dup(arr):
    result = []
    dup = []
    for val in li:
        if val not in result:
            result.append(val)
        else:
            dup.append(val)
    return result + dup

print(move_dup(li))
