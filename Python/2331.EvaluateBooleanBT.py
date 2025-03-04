from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        postmat=[]
        def post(root: Optional[TreeNode]):
            if not root: return
            if root.left:
                post(root.left)
            if root.right:
                post(root.right)
            postmat.append(root.val)
        post(root)
        st=[]
        for p in postmat:
            if p==0:
                st.append(False)
            elif p==1:
                st.append(True)
            elif p==2:
                e1,e2=st.pop(), st.pop()
                st.append(e1 or e2)
            elif p==3:
                e1,e2=st.pop(), st.pop()
                st.append(e1 and e2)
        return st[-1]
    
                