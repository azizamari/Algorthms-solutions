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
  
print('preOrder:')
preOrder(newBT) 
