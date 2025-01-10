from typing import List
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans=1
        for n in nums:
            if n==0:
                return 0
            elif n<0:
                ans*=(-1)
        return ans

s=Solution()
print(s.arraySign([-1,-2,-3,-4,3,2,1])) # 1