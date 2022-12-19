# A python3 program to find a peak
#  element using divide and conquer
 
# A binary search based function
# that returns index of a peak element
 
 
def find_peak(arr, low, high, n):
 
    # Find index of middle element
    mid = (low +high) // 2
 
    # Compare middle element with its
    # neighbours (if neighbours exist)

    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and
        (mid == n - 1 or arr[mid + 1] <= arr[mid])):
        return mid
 
 
    # If middle element is not peak and
    # its left neighbour is greater
    # than it, then left half must
    # have a peak element
    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return find_peak(arr, low, (mid - 1), n)
 
    # If middle element is not peak and
    # its right neighbour is greater
    # than it, then right half must
    # have a peak element
    else:
        return find_peak(arr, (mid + 1), high, n)

li = [10,9,8,7,6,5,4]
print(find_peak(li, 0, len(li)-1, len(li)))