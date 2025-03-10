from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,r=0,len(nums)-1
        i=0
        while i<=r:
            if nums[i]==0:
                nums[i],nums[l]=nums[l],nums[i]
                l+=1
                i+=1
            elif nums[i]==2:
                nums[i],nums[r]=nums[r],nums[i]
                r-=1
            else:
                i+=1
            

s=Solution()
s.sortColors([2,0,2,1,1,0])
s.sortColors([2,0,1])
s.sortColors([1,2,0])
s.sortColors([2,0])