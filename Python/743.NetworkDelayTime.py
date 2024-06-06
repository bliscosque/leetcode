from typing import List

import heapq
class Solution:
    def dijkstra(self, G, start):
        n=len(G)
        distances=[float('inf')]*n
        distances[start]=0
        priority_queue=[(0,start)]
        heapq.heapify(priority_queue)
        visited=set()

        while priority_queue:
            cur_distance,cur_vertex=heapq.heappop(priority_queue)
            if cur_vertex in visited:
                continue
            visited.add(cur_vertex)

            for neighbor, weight in G[cur_vertex]:
                distance=cur_distance+weight
                if distance < distances[neighbor]:
                    distances[neighbor]=distance
                    heapq.heappush(priority_queue,(distance, neighbor))
        
        return distances

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        G={i:[] for i in range(n)}
        for u,v,w in times:
            G[u-1].append((v-1,w))
        print(G)
    
        distances=self.dijkstra(G,k-1)
        max_distance=max(distances)
        return max_distance if max_distance!=float('inf') else -1

        
        

s=Solution()
print(s.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2)) # 2
print(s.networkDelayTime(times = [[1,2,1]], n = 2, k = 1)) # 2
print(s.networkDelayTime(times = [[1,2,1]], n = 2, k = 2)) # -1