

def merge_sort(arr):
    
  print('array:%r' % arr)
  if len(arr)>1:
    mid = len(arr) // 2
    
    lefthalf = arr[:mid]
    righthalf = arr[mid:]

    print('lefthalf:%s' % lefthalf)
    print('righthalf:%s' % righthalf)
    merge_sort(lefthalf)
    merge_sort(righthalf)
    print('Entering to checks')
    i = 0
    j = 0
    k = 0
    print('lefthalf:%s' % lefthalf)
    print('righthalf:%s' % righthalf)
    while i < len(lefthalf) and j<len(righthalf):
        if lefthalf[i] < righthalf[j]:
            arr[k] = lefthalf[i]
            i += 1
        else:
            arr[k] = righthalf[j]
            j += 1
        k += 1

    while i < len(lefthalf):
        arr[k] = lefthalf[i]
        i += 1
        k += 1

    while j < len(righthalf):
        arr[k] = righthalf[j]
        j += 1
        k += 1

    return arr

print(merge_sort([5,1,4,3,2,7,6]))
        
    
