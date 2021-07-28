class TreeNode:
    def __init__(self,value):
        self.value = value
        self.right =None
        self.left =None

def preOrder(root):
    if root is not None:
        print(root.value,end='')
        preOrder(root.left)
        preOrder(root.right)
    else:return
def invert(root):
    if root is None:return root
    invert(root.left)
    invert(root.right)
    root.left,root.right=root.right,root.left
    return root

newBT=TreeNode(0)
newBT.left=TreeNode(1)
newBT.right=TreeNode(2)
newBT.left.left=TreeNode(3)
newBT.left.right=TreeNode(4)
newBT.right.left=TreeNode(5)
newBT.right.right=TreeNode(6)
preOrder(newBT)
print("\nInversing the tree...")
inverse(newBT)
preOrder(newBT)