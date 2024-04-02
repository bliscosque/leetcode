from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printTreePre(t):
    if not t: return
    print(t.val,sep=' ')
    printTreePre(t.left)
    printTreePre(t.right)



class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return
        root.left,root.right=root.right,root.left
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root


s=Solution()
t1=TreeNode(4,TreeNode(2,TreeNode(1),TreeNode(3)),TreeNode(7,TreeNode(6),TreeNode(9)))
printTreePre(t1)
print()
printTreePre(s.invertTree(t1))