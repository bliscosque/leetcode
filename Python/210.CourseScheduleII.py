from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph={v:[] for v in range(numCourses)}
        
        for pr in prerequisites:
            c,cpr=pr
            graph[cpr].append(c)

        visited={v:False for v in graph}
        rec_stack={v:False for v in graph}
        stack=[]
        
        def dfs(v):
            visited[v]=True
            rec_stack[v]=True
            for neighbor in graph[v]:
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
                elif rec_stack[neighbor]:
                    return True
            stack.append(v)
            rec_stack[v]=False
            return False
        
        for v in graph:
            if not visited[v]:
                if dfs(v): 
                    return [] # has cycle, return empty
        
        return stack[::-1]


s=Solution()
print(s.findOrder(2,[[1,0]]))
print(s.findOrder(4,[[1,0],[2,0],[3,1],[3,2]]))
print(s.findOrder(1,[]))
print(s.findOrder(2,[[0,1],[1,0]]))