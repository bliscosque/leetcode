from typing import List
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pq=[]
        ans=[]
        for i in range(k):
            heapq.heappush(pq,(-nums[i],i))
        el=heapq.heappop(pq)
        ans.append(-el[0])
        heapq.heappush(pq,el)

        for i in range(k,len(nums)):
            heapq.heappush(pq,(-nums[i],i))
            el=heapq.heappop(pq)
            while el[1]<=i-k:
                el=heapq.heappop(pq)
            ans.append(el[0]*-1)
            heapq.heappush(pq,el)
        return ans


s=Solution()
print(s.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3)) # [3,3,5,5,6,7]
print(s.maxSlidingWindow(nums = [1], k = 1)) # [1]
print(s.maxSlidingWindow([1,-1],1))