# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def postorderTraversal_int(root):
            if not root: return
            postorderTraversal_int(root.left)
            postorderTraversal_int(root.right)
            ans.append(root.val)
        postorderTraversal_int(root)
        return ans