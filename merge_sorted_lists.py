def merge_sorted(li1, li2):
  i = 0
  j = 0
  res = []
  while i < len(li1) and j < len(li2):
    if li1[i] < li2[j]:
      res.append(li1[i])
      i += 1
    else:
      res.append(li2[j])
      j += 1

  return res + li1[i:] + li2[j:]

print merge_sorted([1,3,5,7], [2,4,6])
