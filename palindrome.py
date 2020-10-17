def is_palindrome(s):
  return s == s[::-1]

def is_palin(s):
  print s
  i = 0
  j = len(s)-1
  while i < j:
    if s[i] != s[j]:
      return False
    i+=1
    j-=1
  return True

print is_palindrome('malayalam')
print is_palin('malayalam')
print is_palin('tamil')

