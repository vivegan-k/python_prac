
def reverse(str):
  if len(str) == 1:
    return str
  else:
    return str[-1] + reverse(str[:-1])

print reverse('abcd')
