

def merge_sort(arr):
    
  print 'array:' , arr
  if len(arr)>1:
    mid = len(arr) / 2
    
    lefthalf = arr[:mid]
    righthalf = arr[mid:]

    print 'lefthalf', lefthalf
    print 'righthalf', righthalf
    merge_sort(lefthalf)
    merge_sort(righthalf)

    i = 0
    j = 0
    k = 0

    while i < len(lefthalf) and j<len(righthalf):
        print 'from double condition'
        print 'i value', i
        print 'lhs', lefthalf
        print 'j value', j
        print 'rhs', righthalf
        if lefthalf[i] < righthalf[j]:
            arr[k] = lefthalf[i]
            i += 1
        else:
            arr[k] = righthalf[j]
            j += 1
        k += 1

    while i < len(lefthalf):
        print 'left condition'
        arr[k] = lefthalf[i]
        i += 1
        k += 1

    while j < len(righthalf):
        print 'right condition'
        arr[k] = righthalf[j]
        j += 1
        k += 1

    print 'Merging', arr
    return arr

print merge_sort([5,1,4,3,2,7,6])
        
    
