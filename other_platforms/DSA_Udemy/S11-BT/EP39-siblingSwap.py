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
        

# so far my code does not work if nodes have values that are repeated
def isSiblingsSwap(t1,t2):
    q=[t1]
    dct1={}
    while q:
        par=q.pop()
        c1,c2=par.left,par.right
        dct1[par.key]=set()
        if c1:
            q.append(c1)
            dct1[par.key].add(c1.key)
        if c2: 
            q.append(c2)
            dct1[par.key].add(c2.key)
    
    q=[t2]
    dct2={}
    while q:
        par=q.pop()
        c1,c2=par.left,par.right
        dct2[par.key]=set()
        if c1:
            q.append(c1)
            dct2[par.key].add(c1.key)
        if c2: 
            q.append(c2)
            dct2[par.key].add(c2.key)
    
    print(dct1,dct2)
    return dct1==dct2

t1=Node(6,   Node(3,Node(1),Node(7)),   Node(8,Node(4,Node(8),Node(9)),Node(2,None,Node(10))))
t2=Node(6,Node(8,Node(2,Node(10)),Node(4,Node(8),Node(9))),Node(3,Node(7),Node(1)))
#printTreeIn(t1)
#print()
#printTreeIn(t2)

print(isSiblingsSwap(t1,t2))