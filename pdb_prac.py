import pdb

def add(i,j):
  k = i+j
  return k

x = [1,2,3]
y = 2
z = 3

pdb.set_trace()
sum = add(y,z)
print(sum)
print(x + y)
