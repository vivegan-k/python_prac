"""

4

   1
  121
 12321
1234321

"""

def triangle(n):
  for i in range(1,n+1):
    space = " " * (n-i)
    middle = "".join([str(j) for j in range(1,i+1)])
    end = middle[:-1][::-1]
    print space + middle + end

triangle(4)
