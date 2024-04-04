from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root or (not root.left and not root.right): return True
        isBal=True
        if root.left and root.right: isBal=-1<=self.maxDepth(root.left)-self.maxDepth(root.right)<=1
        if root.left: 
            isBal=isBal and self.isBalanced(root.left)
            if not root.right:
                if self.maxDepth(root.left)>1: return False
        if root.right: 
            isBal=isBal and self.isBalanced(root.right)
            if not root.left:
                if self.maxDepth(root.right)>1: return False
        return isBal

    def maxDepth(self, root):
        if not root: return 0
        return 1+max(self.maxDepth(root.right),self.maxDepth(root.left))

s=Solution()
t1=TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
# print(s.isBalanced(t1)) # True

t2=TreeNode(1,None,TreeNode(2,None,TreeNode(3)))
# print(s.isBalanced(t2)) # False

t3=TreeNode(1,TreeNode(2),None)
print(s.isBalanced(t3)) # True