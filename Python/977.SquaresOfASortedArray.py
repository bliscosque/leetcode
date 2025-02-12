from typing import List        
import heapq
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        h=[]
        ans=[]
        for n in nums:
            heapq.heappush(h,n*n)
        while h:
            ans.append(heapq.heappop(h))

        return ans

s=Solution()
print(s.sortedSquares([-4,-1,0,3,10]))