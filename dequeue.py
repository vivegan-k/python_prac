# Dequeue(pronounced as dequeue) also known as double-ended queue,
# is an ordered collection of items similar to the queue.

#it has two ends, a front and a rear, and the items remain positioned in the collection

#New items can be added at either the front or the rear

#Likewise items can be removed either of the end

class Dequeue():

  def __init__(self):
    self.items = []

  def addFront(self, item):
    self.items.append(item)

  def addRear(self, item):
    self.items.insert(0, item)

  def removeFront(self):
    self.items.pop()

  def removeRear(self):
    self.items.pop(0)

  def isEmpty(self):
    return self.items == []

  def size(self):
    return len(self.items)
