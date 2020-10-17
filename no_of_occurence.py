def no_of_occurence(arr, val):
  count = 0
  for i in arr:
    if val == i:
      count += 1
  return count

print no_of_occurence([5,4,6,7,4,3,1,4], 4)
