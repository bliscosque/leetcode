from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph={vertex:[] for vertex in range(numCourses)}
        for item in prerequisites:
            c,pre=item
            graph[c].append(pre)
        
        visited={vertex:False for vertex in graph}
        rec_stack={vertex:False for vertex in graph} # recursion stack
        
        def dfs_cycle_directed(vertex,rec_stack):
            #print(vertex, rec_stack)
            visited[vertex]=True
            rec_stack[vertex]=True

            for neighbor in graph[vertex]:
                if not visited[neighbor]:
                    if dfs_cycle_directed(neighbor, rec_stack): return True
                elif rec_stack[neighbor]: 
                    return True

            rec_stack[vertex]=False
            return False

        for vertex in graph:
            if not visited[vertex]:
                if dfs_cycle_directed(vertex,rec_stack):
                    return False # has cycle...cannot finish
        return True # does not have cycle... can finish
        



s=Solution()
print(s.canFinish(2,[[1,0]])) # True
print(s.canFinish(2,[[1,0],[0,1]])) #False

print(s.canFinish(2,[[0,1]])) # True