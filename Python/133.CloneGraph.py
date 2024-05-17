from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def constructFromAdj(adj):
    nodes=[]
    nnodes=len(adj)
    for i in range(nnodes):
        nodes.append(Node(i+1))
    #print(nodes)
    
    for idx,neighbors in enumerate(adj, start=1):
        for el in neighbors:
            nodes[idx-1].neighbors.append(nodes[el-1])

    return nodes

def printfromAdj(nodes):
    for n in nodes:
        print(n.val, end='[')
        for adj in n.neighbors:
            print(adj.val, end=',')
        print(']')

from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None or not node: return None
        if node.neighbors==[]: return Node(1)
        maxnode=0
        nodes=[]
        visited=set()
        dq = deque()
        for i in range(100):
            nodes.append(Node(i+1))
        dq.append(node)
        visited.add(node.val)
        while dq:
            n=dq.pop()
            maxnode=max(maxnode,n.val)
            for neighbor in n.neighbors:
                if neighbor.val not in visited: 
                    dq.append(neighbor)
                    visited.add(neighbor.val)
                nodes[n.val-1].neighbors.append(nodes[neighbor.val-1])
        printfromAdj(nodes[0:maxnode])
        return nodes[0]



s=Solution()
adjList = [[2,4],[1,3],[2,4],[1,3]]
g1=constructFromAdj(adjList)
#printfromAdj(g1)
s.cloneGraph(g1[0])

g2=constructFromAdj([[]])
s.cloneGraph(g2[0])

s.cloneGraph(None)