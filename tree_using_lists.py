#Creating a tree using lists

def BinaryTree(root):
    return [root,[],[]]

def insertLeft(root,value):
    t = root.pop(1)
    if len(t)>1:
        return [root,t,[]]
    else:
        return [root,[],[]]


def insertRight(root, value):
    t = root.pop(2)
    if len(t) > 1:
        return [root,[],t]
    else:
        return [root,[],[]]

def getLeft(root):
    return root[1]

def getRight(root):
    return root[2]


    
