def array_pair_sum(arr, k):
    print arr
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

def find_sum_of_two(A, val):
  found_values = set()
  res = []
  for a in A:
    if val - a in found_values:
      #return True
      res.append([a, val - a])
    found_values.add(a)
    
  return res

print 'final output %r' %array_pair_sum([1,5,3,2,2,-1],4)
print 'final output %r' %find_sum_of_two([1,5,3,2,2,-1],4)
            
