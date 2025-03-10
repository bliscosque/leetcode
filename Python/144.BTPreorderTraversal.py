from typing import List, Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def preorderTraversal_int(root):
            if not root: return
            ans.append(root.val)
            preorderTraversal_int(root.left)
            preorderTraversal_int(root.right)
        preorderTraversal_int(root)
        return ans