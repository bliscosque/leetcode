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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if p and q:
            if p.val!=q.val: return False
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

s=Solution()
t1=array_to_tree([1,2,3])
t2=array_to_tree([1,2,3])
print(s.isSameTree(t1,t2))

t3=array_to_tree([1,2])
t4=array_to_tree([1,None,2])
print(s.isSameTree(t3,t4))

print(s.isSameTree(array_to_tree([1,2,1]),array_to_tree([1,1,2])))