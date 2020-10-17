#https://javainterviewprogramming.com/amazonproblemsovingfindtheindexoftheelement

def find_index(li,target):
  for i in range(len(li)):
    if li[i] == target:
      return i
    else:
      diff = target - i
      i = i + diff
  return -1

li = [0,1,2,3,4,5,4,3,2,1,0,-1,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
print find_index(li, 8)
