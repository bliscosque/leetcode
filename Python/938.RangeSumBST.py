from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        pre=[]
        def preTrav(root):
            if not root: return
            if root.left:
                preTrav(root.left)
            pre.append(root.val)
            if root.right:
                preTrav(root.right)
        preTrav(root)
        ans=0
        for i in pre:
            ans+=i if low<=i<=high else 0
        return ans
