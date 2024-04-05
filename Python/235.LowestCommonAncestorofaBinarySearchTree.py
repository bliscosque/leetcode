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

class Solution:
    def searchPath(self,root:'TreeNode',node:'TreeNode'):
        ans=[root]
        while (node.val!=root.val):
            if root.val<node.val:
                root=root.right
            else:
                root=root.left
            ans.append(root)
        return ans

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pp=self.searchPath(root,p)
        #for e in pp:
        #    print(e.val)
        pq=self.searchPath(root,q)
        for el in pp[::-1]:
            if el in pq: return el

s=Solution()
t=array_to_tree([6,2,8,0,4,7,9,None,None,3,5])
print(s.lowestCommonAncestor(t,t.left,t.right).val) #2,8, LCA=6(root)

print(s.lowestCommonAncestor(t,t.left,t.left.right).val) #2,4, LCA=2(root)

t1=array_to_tree([2,1])
print(s.lowestCommonAncestor(t1,t1,t1.left).val) #2,1, LCA=2(root)
