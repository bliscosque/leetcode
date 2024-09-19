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
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans=""
        def ser_int(root):
            nonlocal ans
            if not root: return
            ans+=str(root.val)
            if root.left or root.right:
                ans+="("
                if root.left:
                    ser_int(root.left)
                ans+=","
                if root.right:
                    ser_int(root.right)
                ans+=")"
            return ans
        ser_int(root)
        print(ans)
        return ans
        

    def split_outside_parentheses(seld,s:str):
        ans=[]
        cur=[]
        open_par=0
        for ch in s:
            if ch=='(':
                open_par+=1
            elif ch==")":
                open_par-=1
            elif ch=="," and open_par==0:
                ans.append(''.join(cur))
                cur=[]
                continue
            cur.append(ch)
        ans.append(''.join(cur))
        return ans


    def deserialize(self, data:str):
        if data=="":
            return None
        if data.count('(')==0:
            return TreeNode(int(data))

        val=data.split("(",1)[0]
        rem=data.split("(",1)[1][:-1]
        ans=TreeNode(int(val))
        if rem!="":
            l,r=self.split_outside_parentheses(rem)
            ans.left=self.deserialize(l)
            ans.right=self.deserialize(r)

        return ans
        

root=array_to_tree([1,2,3,None,None,4,5])
ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root))
printTreePre(ans)

root2=array_to_tree([])
ans2 = deser.deserialize(ser.serialize(root2))

root3=array_to_tree([1,2])
ans3 = deser.deserialize(ser.serialize(root3))