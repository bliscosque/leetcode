from typing import List
import math
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        G={v:[] for v in range(n) }
        for u,v,w in flights:
            G[u].append((v,w))
        
        distances=[math.inf]*n

        pq=[(0,0,src)] #priority queue (dist,num_stops,vertex)
        heapq.heapify(pq)

        while pq:
            cur_distance, n_stops, cur_V = heapq.heappop(pq)
            
            if cur_V==dst:
                return cur_distance

            if n_stops==k+1:
                continue
            
            for neighbor,weight in G[cur_V]:
                distance=cur_distance+weight
                heapq.heappush(pq,(distance,n_stops+1,neighbor))
        
        
        return -1
        # Brute force + Backtracking - TLE        
        #visited=set()
        #ans=math.inf

        #print(G)
        #def try_all(v, sum_weight,stops):
        #    nonlocal ans
        #    #print(v,sum_weight,stops)
        #    if stops<0: 
        #        return
        #    if v==dst:
        #        #print(ans)
        #        ans=min(ans,sum_weight)
        #        return

        #    visited.add(v)
        #    for ngb,w in G[v]:
        #        if ngb not in visited:
        #            try_all(ngb, sum_weight+w,stops-1)
        #    visited.remove(v)

        #try_all(src,0,k+1)
        
        #return ans if ans!=math.inf else -1



s=Solution()
print(s.findCheapestPrice(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1)) # 700
print(s.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1)) # 200
print(s.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0)) #500
print(s.findCheapestPrice(5,[[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]],0,2,2))