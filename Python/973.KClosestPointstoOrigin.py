from typing import Optional, List

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h=[] # heap=distances
        hm={} # distance,points
        heapq.heapify(h)
        for point in points:
            d=(point[0]**2+point[1]**2)**0.5
            #print(d)
            heapq.heappush(h,d)
            if d not in hm:
                hm[d]=[[point[0],point[1]]]
            else: 
                hm[d].append([point[0],point[1]])
        #print(h)
        #print(hm)
        cnt=k
        ans=[]
        while cnt>0:
            el=heapq.heappop(h)
            ans.extend(hm[el])
            cnt-=len(hm[el])
        return ans

s=Solution()
print(s.kClosest([[1,3],[-2,2]],1))
print(s.kClosest([[3,3],[5,-1],[-2,4]],2))
print(s.kClosest([[0,1],[1,0]],2))
