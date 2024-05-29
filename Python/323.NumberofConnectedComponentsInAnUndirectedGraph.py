from typing import List
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph={v:[] for v in range(n)}
        visited={v:False for v in range(n)}
        for vi,vj in edges:
            graph[vi].append(vj)
            graph[vj].append(vi)

        def dfs(v):
            visited[v]=True
            for neighbor in graph[v]:
                if not visited[neighbor]:
                    dfs(neighbor)

        ans=0

        for v in range(n):
            if not visited[v]: 
                ans+=1
                dfs(v)
        return ans




s=Solution()
print(s.countComponents(3,[[0,1], [0,2]]))
print(s.countComponents(6,[[0,1], [1,2], [2,3], [4,5]]))