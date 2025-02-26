from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        if not root.left and not root.right: #leaf
            return targetSum-root.val==0
        op1=op2=False
        if root.left:
            op1=self.hasPathSum(root.left, targetSum-root.val)
        if root.right:
            op2=self.hasPathSum(root.right,targetSum-root.val)
        return op1 or op2