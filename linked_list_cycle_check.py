def cycle_check(node):
    fast, slow = node, node
    print 'fast:', fast.value
    print 'slow:', slow.value
    while fast and fast.nextnode:
        fast = fast.nextnode
        print 'fast:', fast.value
        print 'slow:', slow.value
        if fast == slow:
            return True
        fast = fast.nextnode
        slow = slow.nextnode
    return False

class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None


# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a # Cycle Here!

print cycle_check(a)
