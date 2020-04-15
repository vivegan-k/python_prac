class BinarySearchTree:

  def __init__(self):
    self.root = None
    self.size = 0

  def length(self):
    return self.size

  def __len__(self):
    return self.size

  def __iter__(self):
    return self.root.__iter__()


class TreeNode:

  def __init__(self, key, value, leftChild=None, rightChild=None, parent=None):

    self.key = key
    self.value = value
    self.leftChild = leftChild
    self.rightChild = rightChild
    self.parent = parent

  def hasLeftChild(self):
    return self.leftChild

  def hasRightChild(self):
    return self.rightChild

  def isLeftChild(self):
    return self.parent and self.leftChild == self

  def isRightChild(self):
    return self.parent and self.rightChild == self

  def isRoot(self):
    return not self.parent

  def isLeaf(self):
    return not (self.leftChild or self.rightChild)

  def hasAnyChildren(self):
    return (self.leftChild or self.rightChild)

  def hasBothChildren(self):
'   return (self.leftChild and self.rightChild)

  def replaceNodeData(self, key, value, lc, rc):
    self.key = key
    self.value = value
    self.leftChild = lc
    self.rightChild = rc
    if self.hasLeftChild():
      self.leftChild.parent = self
    if self.hasRightChildI():
      self.rightChild.parent = self




