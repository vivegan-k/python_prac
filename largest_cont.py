def large_cont(li):
    max = li[0]

    for val in li[1:]:
        if max + val > max:
            print(val)
            max += val
    return max

print(large_cont([1,2,-1,3,4,10,10,-10,-1]))
