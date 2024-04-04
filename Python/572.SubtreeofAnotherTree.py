from typing import Optional
from collections import deque

def printTreePre(t):
    if not t: return
    print(t.val,sep=' ')
    printTreePre(t.left)
    printTreePre(t.right)

def array_to_tree(arr):
    if not arr:
        return None

    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1

    while queue and i < len(arr):
        node = queue.popleft()

        if arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1

        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1

    return root

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if p and q:
            if p.val!=q.val: return False
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot: return False
        if root.val==subRoot.val:
            if self.isSameTree(root,subRoot): return True
        if root:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        return False

s=Solution()
print(s.isSubtree(array_to_tree([3,4,5,1,2]),array_to_tree([4,1,2]))) # True
print(s.isSubtree(array_to_tree([3,4,5,1,2,None,None,None,None,0]),array_to_tree([4,1,2]))) # False


