from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2: return None
        root=TreeNode(0)
        if root1 and root2:
            root.val+=root1.val
            root.val+=root2.val
            root.left=self.mergeTrees(root1.left,root2.left)
            root.right=self.mergeTrees(root1.right,root2.right)
        elif root1:
            root.val+=root1.val
            root.left=self.mergeTrees(root1.left,None)
            root.right=self.mergeTrees(root1.right,None)
        elif root2:
            root.val+=root2.val
            root.left=self.mergeTrees(None,root2.left)
            root.right=self.mergeTrees(None,root2.right)
        return root
            
        

s=Solution()
