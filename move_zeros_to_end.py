def move_zeros(arr):
  zeroes = []
  res = []
  for i in range(len(arr)):
    if arr[i] == 0:
      zeroes.append(0)
    else:
      res.append(arr[i])
  res.extend(zeroes)
  return res

print move_zeros([1,2,0,3,0,4,5,0])
       
