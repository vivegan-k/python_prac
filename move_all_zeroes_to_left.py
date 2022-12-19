arr = [1,0,2,3,0,5,6,0,0]

def move_zeroes(li):
    result = []
    for val in arr:
        if val == 0:
            result.insert(0,0)
        else:
            result.append(val)
    return result

print(move_zeroes(arr))
        
