def largest_cont_sum(li):
    if len(arr) == 0:
        return 0
    current_sum = max_sum = li[-1]

    for num in li[2:]:
        current_sum = max(num, current_sum+num)
        max_sum = max(current_sum, max_sum)
        
    return max_sum
