class BST:
    def __init__(self, data):
        self.data = data
        self.left=None
        self.right=None
def insertNode(root,value):
    if root.data==None:
        root.data=value
    elif root.data>=value:
        if root.left is None:
            root.left=BST(value)
        else:
            insertNode(root.left,value)
    else:
        if root.right is None:
            root.right=BST(value)
        else:
            insertNode(root.right,value)
    return "Node successfuly inserted"
def inOrder(root):
    if root is not None:
        inOrder(root.left)
        print(root.data,' ',end='')
        inOrder(root.right)
    else:return



newBST=BST(None)
insertNode(newBST,15)
insertNode(newBST,30)
insertNode(newBST,5)
insertNode(newBST,1)
insertNode(newBST,189)
insertNode(newBST,12)
insertNode(newBST,15)
insertNode(newBST,8)
print(newBST.data)
print(newBST.left.data)
print(newBST.right.data)
print(newBST.left.left.data)
inOrder(newBST)