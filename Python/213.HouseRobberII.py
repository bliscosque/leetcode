from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        robs={}
        n=len(nums)

        #edge case = 1 elem
        if n==1: 
            return nums[0]

        def rob_int(i):
            nonlocal n
            
            if i in robs: return robs[i]
            
            if i>=n:
                return 0
            op1=nums[i]+rob_int(i+2)
            op2=rob_int(i+1)
            robs[i]=max(op1,op2)
            return robs[i]
        
        op1=rob_int(1) # dont 1st house
        
        robs.clear()
        n-=1
        op2=rob_int(0) # can rob the first... but don't include last one

        return max(op1,op2)



s=Solution()
print(s.rob([2,3,2])) # 3
print(s.rob([1,2,3,1])) # 4
print(s.rob([1,2,3])) # 3
print(s.rob([1])) # 1