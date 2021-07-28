# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def sameTree(p,q):
    if p==None or q==None:return q==p
    if not p.val==q.val: return False
    return sameTree(p.left,q.left) and sameTree(p.right,q.right)