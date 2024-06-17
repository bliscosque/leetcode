from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        robs={}
        def rob_int(i):
            if i in robs: 
                return robs[i]
            if i>=len(nums):
                return 0
            op1=nums[i]+rob_int(i+2) #rob curr
            op2=rob_int(i+1) #don't rob curr
            robs[i]=max(op1,op2)
            return robs[i]
        return rob_int(0)

s=Solution()
print(s.rob([1,2,3,1])) # 4 (1+3)
print(s.rob([2,7,9,3,1])) #12
print(s.rob([183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]))

