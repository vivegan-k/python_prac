def find_missing(li):
  """
  Find the missing number in the array
  You are given an array of positive numbers from 1 to n, 
  such that all numbers from 1 to n are present except one number x. 
  You have to find x. The input array is not sorted. 
  Look at the below array and give it a try before checking the solution.
  """
  actual_sum = sum(li)
  print actual_sum

  n = len(li) + 1

  expected_sum = ( n * (n + 1) ) / 2
  print expected_sum

  return expected_sum - actual_sum

print find_missing([7,4,2,8,5,3,1])
