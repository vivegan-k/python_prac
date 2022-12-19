class DoublyLinkedList(object):
    def __init__(self, value) -> None:
        self.value = value
        self.nextnode = None
        self.prevnode = None

node1 = DoublyLinkedList(1)
node2 = DoublyLinkedList(2)
node3 = DoublyLinkedList(3)

node1.nextnode = node2
node2.nextnode = node3

node2.prevnode = node1
node3.prevnode = node2

print(node1.nextnode.value) # 2
print(node1.prevnode) # None