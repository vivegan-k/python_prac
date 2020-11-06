# Python program to find
# number of pairs with
# a given sum in a sorted
# and rotated array.

# This function returns
# count of number of pairs
# with sum equals to x.
def pairsInSortedRotated(arr, n, x):
    # Find the pivot element.
    # Pivot element is largest
    # element of array.
    i = 0
    for i in range(n):
        if arr[i] > arr[i + 1]:
            break

    # l is index of
    # smallest element.
    l = (i + 1) % n

    # r is index of
    # largest element.
    r = i
    print(l, r)

    # Variable to store
    # count of number
    # of pairs.
    cnt = 0

    # Find sum of pair
    # formed by arr[l]
    # and arr[r] and
    # update l, r and
    # cnt accordingly.
    while (l != r):

        # If we find a pair
        # with sum x, then
        # increment cnt, move
        # l and r to next element.
        if arr[l] + arr[r] == x:
            cnt += 1

            # This condition is
            # required to be checked,
            # otherwise l and r will
            # cross each other and
            # loop will never terminate.
            if l == (n + r - 1) % n:
                return cnt

            l = (l + 1) % n
            r = (r - 1 + n) % n

        # If current pair sum
        # is less, move to
        # the higher sum side.
        elif arr[l] + arr[r] < x:
            l = (l + 1) % n

        # If current pair sum
        # is greater, move to
        # the lower sum side.
        else:
            print('entered')
            r = (r - 1 + n) % n
        print(l,r)

    return cnt


# Driver Code
arr = [11, 15, 6, 7, 9, 10]
s = 16

print(pairsInSortedRotated(arr, 6, s))


