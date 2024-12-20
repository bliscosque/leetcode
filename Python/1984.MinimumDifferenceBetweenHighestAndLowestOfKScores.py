from typing import List
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k==1: return 0
        k-=1
        nums.sort()
        ans=float('inf')
        for i in range(len(nums)-k):
            n1,n2=nums[i],nums[i+k]
            ans=min(ans,n2-n1)
        return ans


s=Solution()
print(s.minimumDifference(nums = [90], k = 1))
print(s.minimumDifference(nums = [9,4,1,7], k = 2))