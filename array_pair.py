def array_pair_sum1(array, sum):
    output = set()
    seen = set()
    if len(array) < 1:
        return
    for num in array:
        target = sum - num
        if target in seen:
            output.add( (min(target, num), max(target, num)))
        else:
            seen.add(num)

    return output

def array_pair_sum(array, sum):
    res = []
    found_values = set()
    for val in array:
        target = sum - val
        if target in found_values:
            res.append([val, target])
        found_values.add(val)
    return res

print(array_pair_sum([1,3,2,2], 4))
