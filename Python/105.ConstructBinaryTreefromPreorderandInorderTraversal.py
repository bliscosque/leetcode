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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder)==0: return None
        t=TreeNode(preorder[0])
        idx_root=inorder.index(preorder[0])
        del preorder[0]
        l_inorder=inorder[0:idx_root]
        r_inorder=inorder[idx_root+1:] if idx_root+1<len(inorder) else []
        t.left=self.buildTree(preorder,l_inorder)
        t.right=self.buildTree(preorder,r_inorder)
        return t

s=Solution()
printTreePre(s.buildTree([3,9,20,15,7],[9,3,15,20,7]))
printTreePre(s.buildTree([-1],[-1]))