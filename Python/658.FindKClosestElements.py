from typing import List
import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        h=[]
        heapq.heapify(h)
        for el in arr:
            dst=abs(el-x)
            heapq.heappush(h,(dst,el))
        #print(h)
        ans=[]
        while k>0:
            ans.append(heapq.heappop(h)[1])
            k-=1
        ans.sort()
        return ans


s=Solution()
print(s.findClosestElements(arr = [1,2,3,4,5], k = 4, x = 3)) #[1,2,3,4]
print(s.findClosestElements(arr = [1,2,3,4,5], k = 4, x = -1)) #[1,2,3,4]