from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={}
        def findTargetSumWays_int(i, par):
            if (i,par) in dp:
                return dp[(i,par)]
            if i==len(nums):
                if par==target:
                    return 1
                else:
                    return 0
            ans=findTargetSumWays_int(i+1,par+nums[i])
            ans+=findTargetSumWays_int(i+1,par-nums[i])
            dp[(i,par)]=ans
            return ans
        return findTargetSumWays_int(0,0)


s=Solution()
print(s.findTargetSumWays([1,1,1,1,1],3)) #5
print(s.findTargetSumWays([1],1)) #1