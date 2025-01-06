from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm={0:1} #prefix_sum -> count
        curSum=0
        ans=0
        for n in nums:
            curSum+=n
            diff=curSum-k
            ans+=hm.get(diff,0)
            hm[curSum]=1+hm.get(curSum,0)
        return ans


        

s=Solution()
print(s.subarraySum(nums = [1,1,1], k = 2)) #2
print(s.subarraySum(nums = [1,2,3], k = 3)) #2