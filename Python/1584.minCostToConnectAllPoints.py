from typing import List

class UnionFind:
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[0]*n

    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        root_x=self.find(x)
        root_y=self.find(y)
        if root_x != root_y:
            if self.rank[root_x]<self.rank[root_y]:
                root_x,root_y=root_y,root_x
            self.parent[root_y]=root_x
            if self.rank[root_x]==self.rank[root_y]:
                self.rank[root_x]+=1

def kruskal(edges,n):
    edges.sort(key=lambda x:x[2])
    uf=UnionFind(n)
    mst=[]
    for u,v,weight in edges:
        if uf.find(u)!=uf.find(v):
            uf.union(u,v)
            mst.append((u,v,weight))
    return mst


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        edges=[]
        for i in range(n-1):
            for j in range(i+1,n):
                x,y=points[i], points[j]
                d=abs(x[0]-y[0])+abs(x[1]-y[1])
                edges.append([i,j,d])
                edges.append([j,i,d])
        
        mst=kruskal(edges,n)
        #print(mst)
        ans=0
        for el in mst:
            ans+=el[2]
        return ans



s=Solution()
print(s.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
print(s.minCostConnectPoints([[3,12],[-2,5],[-4,1]]))
