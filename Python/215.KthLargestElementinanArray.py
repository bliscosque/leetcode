from typing import Optional, List

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        return heapq.nlargest(k,nums)[-1]

s=Solution()
print(s.findKthLargest([3,2,1,5,6,4],2))
print(s.findKthLargest([3,2,3,1,2,4,5,5,6],4))