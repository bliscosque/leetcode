class Node:
    def __init__(self,key=None,left=None,right=None):
        self.key=key
        self.left=left
        self.right=right

def printTreeIn(n):
    if not n: return
    printTreeIn(n.left)
    print(n.key, end=" ")
    printTreeIn(n.right)
        

def isSiblingsSwap(t1,t2):
    def serialize(root):
        if not root: return "null"
        left=serialize(root.left)
        right=serialize(root.right)

        # se left>right, trocamos (para manter sempre normalizado)
        if left>right:
            left,right=right,left
        return f"({root.key},{left},{right})"
    s1=serialize(t1)
    s2=serialize(t2)
    print(s1,s2)
    return s1==s2

t1=Node(6,   Node(3,Node(1),Node(7)),   Node(8,Node(4,Node(7),Node(1)),Node(2,None,Node(3))))
t2=Node(6,Node(8,Node(2,Node(3)),Node(4,Node(1),Node(7))),Node(3,Node(7),Node(1)))
#printTreeIn(t1)
#print()
#printTreeIn(t2)

print(isSiblingsSwap(t1,t2))