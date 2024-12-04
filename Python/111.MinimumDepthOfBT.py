from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def minDepthInt(root):
            if root is None: 
                return float('inf')
            if root.left is None and root.right is None:
                return 1
            return 1+min(minDepthInt(root.left),minDepthInt(root.right))

        if root is None: 
            return 0
        else: 
            return minDepthInt(root)


