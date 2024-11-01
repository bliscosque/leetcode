from typing import List
import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        visited=set()

        pq=[(grid[0][0],(0,0))] # distance,(l,c)
        heapq.heapify(pq)
        movx,movy=[0,0,1,-1],[1,-1,0,0]
        min_max_time=0

        while pq:
            cur_time,cur_vertex=heapq.heappop(pq)
            #print(visited)
            #print(cur_time, cur_vertex)
            #print(pq)
            #print()
            min_max_time=max(min_max_time,cur_time)

            if cur_vertex==(n-1,n-1): return min_max_time

            if cur_vertex in visited: continue  
            
            visited.add(cur_vertex)          

            for k in range(4):
                nx,ny=cur_vertex[0]+movx[k],cur_vertex[1]+movy[k]
                if 0<=nx<n and 0<=ny<n:
                    min_time=grid[nx][ny]
                    heapq.heappush(pq,(min_time,(nx,ny)))
        


s=Solution()
print(s.swimInWater([[0,2],[1,3]]))
print(s.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))
print(s.swimInWater([[3,2],[0,1]]))