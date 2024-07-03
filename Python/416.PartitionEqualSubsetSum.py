from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sTotal=sum(nums)
        if sTotal%2!=0: return False
        searchedSum=sTotal//2
        dp={}
        nums.sort(reverse=True) # otimização para memória

        def f_int(i,cur_sum):
            nonlocal searchedSum
            if cur_sum==searchedSum: return True
            if cur_sum > searchedSum or i == len(nums): return False

            if (i,cur_sum) in dp: return dp[(i,cur_sum)]

            op1=f_int(i+1, cur_sum+nums[i])
            if op1: return True # otimização para memória
            op2=f_int(i+1, cur_sum)
            if op2: return True # otimização para memória

            dp[(i,cur_sum)]=op1 or op2
            return dp[(i,cur_sum)]
        
        return f_int(0, 0)
    
s=Solution()
print(s.canPartition([1,5,11,5]))
nums=[100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,99,97]
print(s.canPartition(nums))