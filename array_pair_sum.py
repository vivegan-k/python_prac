def array_pair_sum(arr, k):

    seen = set()
    output = set()

    for num in arr:
        print 'new iteration'
        target = k - num
        print 'target %d' %target 
        if target not in seen:
            seen.add(num)
            print 'seen %r' %seen
        else:
            output.add((min(num,target) , max(num, target)))
            print 'output %r' %output 
    return output

print 'final output %r' %array_pair_sum([1,5,3,2,2,-1],4)
            
