from typing import Optional, List
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

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        trav=[]
        def kthSmallest_int(root):
            if not root: return
            kthSmallest_int(root.left)
            trav.append(root.val)
            kthSmallest_int(root.right)
        kthSmallest_int(root)
        return trav[k-1]

s=Solution()
t1=array_to_tree([3,1,4,None,2])
print(s.kthSmallest(t1,1))
t2=array_to_tree([5,3,6,2,4,None,None,1])
print(s.kthSmallest(t2,3))
