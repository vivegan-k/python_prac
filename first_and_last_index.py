# Find the index of first and last occurence of given number


def find(arr, num):
    result = [-1,-1]
    first_index = None
    last_index = None
    for i in range(len(arr)):
        if arr[i] == num:
            first_index = i
            break
    if first_index:
        remaining_list = arr[first_index:]
        for j in range(len(remaining_list)):
            if remaining_list[j] == num:
                last_index = j
            elif remaining_list[j] > num:
                break
    if first_index:
        result[0] = first_index
    if last_index:
        result[1] = first_index + last_index
    return result

print(find([1,2,3,5,5,6], 5))

