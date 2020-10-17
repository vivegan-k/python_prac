def is_prime(n):
  print n
  if n==1:
    return False
  elif n == 2:
    return True
  else:
    for i in range(2,n):
      if n%i == 0:
        return False
    return True

print is_prime(17)
print is_prime(36)
print is_prime(2)
print is_prime(1)

def first_n_prime(n):
  result = []
  result.append(2)
  count = n-1
  is_prime = True
  for i in range(3,n):
    for j in range(2,(i//2)+1):
      print i,j
      if i % j == 0:
        is_prime = False
        break
    if is_prime:
      result.append(i)
    is_prime = True
  return result

print first_n_prime(10)

def str_comp(s):
  print s
  first_char= s[0]
  count = 1
  result = []
  for i in range(1, len(s)):
    if s[i] == first_char:
      count += 1
    else:
      result.append(first_char + str(count))
      first_char = s[i]
      count = 1
  result.append(first_char + str(count))
  return ''.join(result)

print str_comp('abbbccd')
print str_comp('aabbbccdd')


