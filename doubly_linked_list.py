class DoublyLinkedList(object):

  def __init__(self, value):
    self.value = value
    self.next_node = None
    self.prev_node = None

a = DoublyLinkedList(1)
b = DoublyLinkedList(2)
c = DoublyLinkedList(3)

a.next_node = b
b.next_node = c

b.prev_node = a
c.prev_node = b
