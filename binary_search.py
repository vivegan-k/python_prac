def binary_search_iterative(arr, ele):

  first = 0
  last = len(arr) - 1
  found = False

  while first <= last and not found:

    mid = (first + last) / 2

    if arr[mid] == ele:
      found = True

    else:
      if arr[mid] <  ele:
        last = mid - 1
      else:
        first = mid + 1

  return found

print binary_search_iterative([1,2,3,4,5], 3)
print binary_search_iterative([1,2,3,4,5], 6)


def binary_search_recursive(arr, ele):

  if len(arr) == 0:
    return False

  else:
    mid = len(arr) / 2

    if arr[mid] == ele:
      return True

    else:
      if ele < arr[mid]:
        return binary_search_recursive(arr[:mid], ele)
      else:
        return binary_search_recursive(arr[mid+1:], ele)


print binary_search_recursive([1,2,3,4,5], 3)
print binary_search_recursive([1,2,3,4,5], 6)
