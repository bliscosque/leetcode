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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        # or in 2 lines...
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        self.md=1
        def mdepth(root,val):
            self.md=max(self.md,val)
            if root.left:
                mdepth(root.left,val+1)
            if root.right:
                mdepth(root.right,val+1)
        mdepth(root,1)
        return self.md

        
s=Solution()
t1=TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
print(s.maxDepth(t1))

t2=TreeNode(1,None,TreeNode(2))
print(s.maxDepth(t2))