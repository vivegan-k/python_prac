def searcharray(arr, l, h, search_key):
    if l > h:
        return -1

    mid = (l + h) // 2

    if arr[mid] == search_key:
        return mid

    # if arr[l...mid] is sorted
    if arr[l] <= arr[mid]:
        if search_key >= arr[l] and search_key <= arr[mid]:
            return searcharray(arr, l, mid-1, search_key)
        return searcharray(arr, mid+1, h, search_key)

    # If arr[l..mid] is not sorted, then arr[mid... h]
    # must be sorted
    if search_key >= arr[mid] and search_key <= arr[h]:
        return searcharray(arr, mid+1, h, search_key)
    return searcharray(arr, l, mid-1, search_key)

li = [5, 6, 7, 1, 2, 3, 4]
print(searcharray(li, 0, len(li)-1, 3))


