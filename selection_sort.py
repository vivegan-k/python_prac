def selection_sort(list):
    for fillslot in range(len(list)-1,0,-1):
        maxpos = 0
        for location in range(1, fillslot+1):
            if list[location] > list[maxpos]:
                maxpos = location

            temp = list[location]
            list[location] = list[maxpos]
            list[maxpos] = temp

    return list

print selection_sort([3,4,1,5,2]) 
