def insertion_sort(list):
    for index in range(1,len(list)):
        position = index
        current_value = list[index]
        while position> 0 and list[position -1]>current_value:
            list[position] = list[position-1]
            position = position -1
        list[position] = current_value
    return list

print insertion_sort([5,4,1,3,2,6])
