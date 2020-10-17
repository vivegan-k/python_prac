def get_min_index(Array, start):
    min_index = start

    start += 1

    while start < len(Array):
        if Array[start] < Array[min_index]:
            min_index = start
        start += 1
    return min_index



def selection_sort(A):
    i = 0

    while i < len(A):
        min_index = get_min_index(A, i)

        if min_index != i:
            A[i], A[min_index] = A[min_index], A[i]
        i += 1
    return  A


A = [5, 2, 6, 7, 2, 1, 0, 3]

print(selection_sort(A))

