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

def preOrder(root):
    if root is not None:
        print(root.value,end='')
        preOrder(root.left)
        preOrder(root.right)
    else:return

def inOrder(root):
    if root is not None:
        preOrder(root.left)
        print(root.value,end='')
        preOrder(root.right)
    else:return

def postOrder(root):
    if root is not None:
        preOrder(root.left)
        preOrder(root.right)
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

print('preOrder:')
preOrder(newBT) 
print('\ninOrder:')
inOrder(newBT) 
print('\npostOrder:')
postOrder(newBT)
print('') 
print(ifNodeExists(newBT,6))