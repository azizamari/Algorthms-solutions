from Queue import Queue

class TreeNode:
    def __init__(self,value):
        self.value = value
        self.right =None
        self.left =None

newBT=TreeNode(0)
newBT.left=TreeNode(1)
newBT.right=TreeNode(2)
newBT.left.left=TreeNode(3)
newBT.left.right=TreeNode(4)
newBT.right.left=TreeNode(5)
newBT.right.right=TreeNode(6)
newBT.left.left.left=TreeNode(69)

def preOrder(root):
    if root is not None:
        print(root.value,end='')
        preOrder(root.left)
        preOrder(root.right)
    else:return

def preOrderSerialize(root):
    if root is None:
        return 'x,'
    leftSer=preOrderSerialize(root.left)
    rightSer=preOrderSerialize(root.right)
    return str(root.value)+','+leftSer+rightSer

def inOrder(root):
    if root is not None:
        inOrder(root.left)
        print(root.value,end='')
        inOrder(root.right)
    else:return

def postOrder(root):
    if root is not None:
        postOrder(root.left)
        postOrder(root.right)
        print(root.value,end='')
    else:
        return    

def ifNodeExists(root, key): 
    if (root == None):
        return False
    if (root.value == key):
        return True
    if ifNodeExists(root.left, key):
        return True 
    return ifNodeExists(root.right, key)

def treeHeight(root):
    if(root == None):
        return -1
    return max(treeHeight(root.left), treeHeight(root.right))+1

def levelOrderTraversal(root):
    if not root:return
    else:
        customQueue=Queue()
        customQueue.enqueue(root)
        while not customQueue.isEmpty():
            root=customQueue.dequeue()
            print(root.value.value)
            if root.value.left is not None:
                customQueue.enqueue(root.value.left)
            if root.value.right is not None:
                customQueue.enqueue(root.value.right)


def elementExistsInTree(root,e):
    if not root:return
    else:
        customQueue=Queue()
        customQueue.enqueue(root)
        while not customQueue.isEmpty():
            root=customQueue.dequeue()
            if e==root.value.value:
                return True
            if root.value.left is not None:
                customQueue.enqueue(root.value.left)
            if root.value.right is not None:
                customQueue.enqueue(root.value.right)
    return False

def insertInTree(root,e):
    if not root:return
    else:
        customQueue=Queue()
        customQueue.enqueue(root)
        while not customQueue.isEmpty():
            root=customQueue.dequeue()
            if root.value.left is None:
                root.value.left=e
                return
            else:
                customQueue.enqueue(root.value.left)
            if root.value.left is None:
                root.value.left=e
                return
            else:
                customQueue.enqueue(root.value.right)


levelOrderTraversal(newBT)
print('preOrder:')
preOrder(newBT) 
print('\ninOrder:')
inOrder(newBT) 
print('\npostOrder:')
postOrder(newBT)
print('') 
print(ifNodeExists(newBT,6))
print(treeHeight(newBT))
print('Serialized')
print(preOrderSerialize(newBT))
print(elementExistsInTree(newBT,15))
insertInTree(newBT,TreeNode(6000))
print('preOrder:')
preOrder(newBT) 