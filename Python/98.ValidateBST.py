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
import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate_int(root,max=math.inf,min=-math.inf):
            if not root: return True
            cur=min<root.val<max
            left=validate_int(root.left,root.val,min)
            right=validate_int(root.right,max,root.val)
            return cur and left and right
        return validate_int(root)

s=Solution()
t1=array_to_tree([2,1,3])
print(s.isValidBST(t1)) # True
t2=array_to_tree([5,1,4,None,None,3,6])
print(s.isValidBST(t2)) # False