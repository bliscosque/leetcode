from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        graph={v:[] for v in range(1,n+1)}
        visited={v:False for v in range(1,n+1)}
        path=[]
        cycles=[]
        found_cycle=False

        for vi,vj in edges:
            graph[vi].append(vj)
            graph[vj].append(vi)
        
        def dfs(v, parent):
            nonlocal found_cycle
            #print(v,visited,path)
            visited[v]=True
            path.append(v)

            for neighbor in graph[v]:
                if neighbor==parent: 
                    continue
                if visited[neighbor]:
                    cycle_start_idx=path.index(neighbor)
                    cycles.append(path[cycle_start_idx:])
                    found_cycle=True
                else:
                    dfs(neighbor,v)
                    if found_cycle:
                        return
            path.pop()


        dfs(1, None)
        cycle=cycles[0]
        #print(cycle, edges) 
        for i in range(n-1,-1,-1):
            vi,vj=edges[i][0],edges[i][1]
            #print(vi,vj)
            #edge case... first ans last elements 
            c1,c2=cycle[0],cycle[-1]
            if vi==c1 and vj==c2 or vi==c2 and vj==c1:
                return [vi,vj]

            for j in range(len(cycle)-1):
                c1,c2=cycle[j],cycle[j+1]
                #print(" ",c1,c2)
                if vi==c1 and vj==c2 or vi==c2 and vj==c1:
                    return [vi,vj]

        


s=Solution()
print(s.findRedundantConnection([[1,2],[1,3],[2,3]]))
print(s.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))