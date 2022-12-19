def bs(arr, val):
    if len(arr) == 0:
        return False
    else:
        mid = len(arr) // 2
        if arr[mid] == val:
            return True
        else:
            if val > arr[mid]:
                return bs(arr[mid+1:],val)
            else:
                return bs(arr[:mid-1], val)
    

print(bs([1,3,5,7,11,15,17,19,25,27],7)) 
