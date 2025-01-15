from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_0=0
        while last_0< len(nums) and nums[last_0]!=0:
                last_0+=1
        last_n0=last_0+1
        while last_n0< len(nums) and nums[last_n0]==0:
                last_n0+=1
        while last_n0<len(nums) and last_n0<len(nums):
            nums[last_n0],nums[last_0]=nums[last_0],nums[last_n0]
            
            while last_0< len(nums) and nums[last_0]!=0:
                last_0+=1
            last_n0=last_0+1
            while last_n0< len(nums) and nums[last_n0]==0:
                last_n0+=1
        return nums
            

s=Solution()
nums = [0,1,0,3,12]
s.moveZeroes(nums)
print(nums)
nums = [0]
s.moveZeroes(nums)
print(nums)