def nth_to_last_node(n, head):

  left_pointer = head
  right_pointer = head

  #Move only right pointer untill it reaches last node

  for i in xrange(n-1):
    if not right_pointer.nextnode:
      raise LookupError('Error: n is longer than linke list')

    right_pointer = right_pointer.nextnode
    print right_pointer.value

  while right_pointer.nextnode:
    left_pointer = left_pointer.nextnode
    right_pointer = right_pointer.nextnode

    print 'left_pointer:', left_pointer.value
    print 'right_pointer:', right_pointer.value

  return left_pointer

#Testing the solution

class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode  = None

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

# This would return the node d with a value of 4, because its the 2nd to last node.
target_node = nth_to_last_node(2, a) 

print target_node.value
