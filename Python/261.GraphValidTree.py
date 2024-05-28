from typing import List
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph={v:[] for v in range(n)}
        visited={v:False for v in range(n)}

        for e1,e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)

        def dfs_cycle_undirected(v,parent):
            visited[v]=True
            for neighbor in graph[v]:
                if not visited[neighbor]:
                    if dfs_cycle_undirected(neighbor,v): return True
                elif neighbor != parent: return True
            return False
        
        has_cycle=dfs_cycle_undirected(0,None)
        #print(has_cycle,visited)
        if not has_cycle and all(visited.values()): return True
        return False

        



s=Solution()
print(s.validTree(5,[[0, 1], [0, 2], [0, 3], [1, 4]]))
print(s.validTree(5,[[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))