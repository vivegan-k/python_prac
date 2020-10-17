def sorting(li):
  new_list = []

  while li:
    print li
    min = li[0]
    for val in li:
      if val < min:
        min = val
    new_list.append(min)
    li.remove(min)
  return new_list

my_list = [-15, -26, 15, 1, 23, -64, 23, 76, -26]
print 'input:', my_list
print sorting(my_list)
