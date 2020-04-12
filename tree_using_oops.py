class BinaryTree(object):

  def __init__(self, rootObj):
    self.key = rootObj # root
    self.leftChild = None
    self.rightChild = None

  def addLeft(self, value):
    if self.leftChild is None:
      self.leftChild = value

    else:
      t = BinaryTree(value)
      t.leftChild = self.leftChild
      self.leftChild = t

  def addRight(self, value):
    if self.rightChild is None:
      self.rightChild = self.rightChild

    else:
      t = BinaryTree(value)
      t.rightChild = self.rightChild
      self.rightChild = t


  def setRoot(self, root):
    self.key = root

  def getRoot(self):
    return self.key

  def getRight(self):
    return self.rightChild

  def getLeft(self):
    return self.leftChild


t = BinaryTree(1)

t.addLeft(2)
t.addRight(3)

print 'root', t.getRoot()
print 'left', t.getLeft()
print 'right', t.getRight()
      
