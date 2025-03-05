from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        inord_m=[]
        def inord(root:Optional[TreeNode]):
            if not root: return
            if root.left:
                inord(root.left)
            inord_m.append(root.val)
            if root.right:
                inord(root.right)

        inord(root)
        min_val=abs(inord_m[0]-inord_m[1])
        for i in range(1,len(inord_m)-1):
            min_val=min(min_val,abs(inord_m[i]-inord_m[i+1]))
        return min_val
