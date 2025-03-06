from typing import Optional
from collections import deque


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

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def issym(r1:Optional[TreeNode], r2:Optional[TreeNode]):
            if not r1 and not r2: return True
            
            if not r1 or not r2: return False

            if r1.val!=r2.val: return False
            
            return issym(r1.left,r2.right) and issym(r1.right,r2.left)
        
        return issym(root.left,root.right)

s=Solution()
t1=array_to_tree([1,2,2,3,4,4,3])
print(s.isSymmetric(t1))
t2=array_to_tree([1,2,2,None,3,None,3])
print(s.isSymmetric(t2))