#Implementation of stack

class Stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        self.items.pop()

    def seek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


    
    
