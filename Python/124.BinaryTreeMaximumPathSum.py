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
    def checkMaxVal(self,root: Optional[TreeNode]):
        if not root: 
            return float('-inf')
        return max(root.val, self.checkMaxVal(root.left), self.checkMaxVal(root.right))


    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxVal=self.checkMaxVal(root)
        if maxVal<0: 
            return maxVal
        
        return self.maxPathSum_int(root)

    def maxPathSum_int(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        if not root.left and not root.right:
            return root.val if root.val > 0 else 0
        maxSumLeft=self.maxPathSum_int(root.left)
        maxSumRight=self.maxPathSum_int(root.right)
        if maxSumLeft<0: maxSumLeft=0
        if maxSumRight<0: maxSumRight=0
        includeRoot=root.val+maxSumLeft+maxSumRight
        print(includeRoot, root.val, maxSumLeft, maxSumRight)
        if includeRoot>maxSumLeft and includeRoot>maxSumRight:
            return includeRoot
        else:
            return max(maxSumLeft,maxSumRight)


t1=array_to_tree([1,2,3])
s=Solution()
#print(s.maxPathSum(t1)) # 6
t2=array_to_tree([-10,9,20,None,None,15,7])
#print(s.maxPathSum(t2)) # 42
t3=array_to_tree([-3])
#print(s.maxPathSum(t3)) # -3
t4=array_to_tree([-2,1])
#print(s.maxPathSum(t4)) # 1
t5=array_to_tree([1,-2,-3,1,3,-2,None,-1])
print(s.maxPathSum(t5)) # 3