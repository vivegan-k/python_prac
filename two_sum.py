# https://www.youtube.com/watch?v=cQ1Oz4ckceM

# arr = [1,3,4,5,7,9,11] target = 9 assuming index starts from 1


def two_sum(arr, target):
    left, right = 0, len(arr) -1
    while left < right:
        currentSum = arr[left] + arr[right]
        if currentSum > target:
            right -= 1
        elif currentSum < target:
            left += 1
        else:
            return [left+1, right+1] # +1 is for asssuming index starts from 1

arr = [1,3,4,5,7,9,11]
print(two_sum(arr, 9))

