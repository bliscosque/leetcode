from typing import List
import math
class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        d={}
        def f_int(i):
            if i in d: return d[i]
            nonlocal n
            if i>=n: return math.inf
            if i==n-1: return 0
            ans=math.inf
            for jump in range(1,nums[i]+1):
                ans=min(ans,1+f_int(i+jump))
            d[i]=ans
            return d[i]
            
        return f_int(0)


s=Solution()
print(s.jump([2,3,1,1,4])) #2
print(s.jump([2,3,0,1,4])) #2