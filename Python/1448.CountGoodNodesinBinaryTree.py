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
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        self.ans=0
        def goodNodes_int(root,max_so_far):
            if not root: return
            if root.val>=max_so_far:
                self.ans+=1
                goodNodes_int(root.left,root.val)
                goodNodes_int(root.right,root.val)
            else:
                goodNodes_int(root.left,max_so_far)
                goodNodes_int(root.right,max_so_far)
        goodNodes_int(root,root.val)
        return self.ans

s=Solution()
t1=array_to_tree([3,1,4,3,None,1,5])
print(s.goodNodes(t1)) # 4