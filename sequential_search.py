
def sequential_search(arr, ele):

  pos = 0
  found = False

  while pos < len(arr) and not found:

    if arr[pos] == ele:
      found = True
    else:
      pos+=1

  return found

print sequential_search([1,4,3,2,5], 2)
print sequential_search([1,4,3,2,5], 6)


def ordered_seq_search(arr, ele):
  """
  Array should be ordered
  """

  pos = 0
  found = False
  stopped = False

  while pos < len(arr) and not found and not stopped:

    if arr[pos] == ele:
      found = True
    else:
      if arr[pos] > ele:
        stopped = True
      else:
         pos+=1
  return found

print ordered_seq_search([1,2,3,4,5], 3)
