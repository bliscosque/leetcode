from typing import Optional

def printTreePre(t):
    if not t: return
    print(t.val,sep=' ')
    printTreePre(t.left)
    printTreePre(t.right)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self,root):
        if not root: return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diam=0
        def diam_int(root):
            if not root: return
            if not root.left and not root.right: return
            maxl=self.maxDepth(root.left) if root.left else 0
            maxr=self.maxDepth(root.right) if root.right else 0
            #print(root.val, maxl, maxr)
            self.max_diam=max(self.max_diam,maxl+maxr)
            diam_int(root.left)
            diam_int(root.right)
        diam_int(root)
        return self.max_diam


s=Solution()
t1=TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3))
#printTreePre(t1)
print(s.diameterOfBinaryTree(t1))

t2=TreeNode(1,TreeNode(2),None)
print(s.diameterOfBinaryTree(t2))

t3=TreeNode(1)
print(s.diameterOfBinaryTree(t3))

t4=TreeNode(2,TreeNode(3,TreeNode(1)))
print(s.diameterOfBinaryTree(t4))
