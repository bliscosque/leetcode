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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        els=[]
        def rightSideView_int(root,pos):
            if not root: return
            if len(els)<=pos:
                els.append([])
            els[pos].append(root.val)
            rightSideView_int(root.left,pos+1)
            rightSideView_int(root.right,pos+1)
        rightSideView_int(root,0)
        ans=[]
        for el in els:
            ans.append(el[-1])
        return ans
            
        


s=Solution()
t1=array_to_tree([1,2,3,None,5,None,4])
print(s.rightSideView(t1))