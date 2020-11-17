def max_diff(li):
  max_val = li[1] - li[0]
  for i in range(2,len(li)):
    if (li[i] - li[i-1]) > max_val:
      max_val = li[i] - li[i-1]
  return max_val

print max_diff([12,11,15,3,10])
      
