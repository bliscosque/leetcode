from typing import List
class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        def count_bits(n):
            ans=0
            while n>0:
                n=n&(n-1)
                ans+=1
            return ans
        ans=0
        for i in range(len(nums)):
            if count_bits(i)==k:
                ans+=nums[i]
        return ans



s=Solution()
print(s.sumIndicesWithKSetBits(nums = [5,10,1,5,2], k = 1)) #13