from typing import List
class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        n=len(nums)
        t=0
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if (nums[i] & nums[j] & nums[k])==0:
                        t+=1
        return t

s=Solution()
print(s.countTriplets([2,1,3])) # 12
print(s.countTriplets([0,0,0])) # 27
