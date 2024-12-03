from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def nextdown(self,node):
        if self.ans: return self.ans
        
        if not node:
            return
        
        left_result=self.nextdown(node.left)
        if left_result: return left_result
        
        if not self.ans:
            self.ans=node
        
        right_result = self.nextdown(node.right)
        if right_result: 
            return right_result 
        
        return self.ans

    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        self.ans=None
        if node.right:
            self.nextdown(node.right)
            return self.ans.val
        
        curr=node
        while curr.parent and curr.parent.right==curr:
            curr=curr.parent

        return curr.parent.val if curr.parent else None
            

            

t1=Node(5)

t1.left=Node(3)
t1.left.parent=t1
t1.right=Node(6)
t1.right.parent=t1

t1.left.left=Node(2)
t1.left.left.parent=t1.left
t1.left.right=Node(4)
t1.left.right.parent=t1.left

t1.left.left.left=Node(1)
t1.left.left.left.parent=t1.left.left

s=Solution()
print(s.inorderSuccessor(t1)) # 6
print(s.inorderSuccessor(t1.left)) # 4
print(s.inorderSuccessor(t1.left.left)) # 3
print(s.inorderSuccessor(t1.right)) # None