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
def searchTree(root, ele):
    if root is None: return False
    if ele == root.data:
        return True
    elif ele>root.data:
        return searchTree(root.right,ele)
    else:
        return searchTree(root.left,ele)

def minValue(root):
    curr=root
    while curr.left is not None:
        curr=curr.left
    return curr

def deleteNode(root,ele):
    if root is None:
        return root
    if root.data>ele:
        root.left=deleteNode(root.left,ele)
    elif root.data<ele:
        root.right=deleteNode(root.right,ele)
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
        if root.right is None:
            temp=root.left
            root=None
            return temp
        temp=minValue(root.right)
        root.data=temp.data
        root.right=deleteNode(root.right,temp.data)
    return root
        

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
deleteNode(newBST,15)
inOrder(newBST)
print()
print(searchTree(newBST,112))