from typing import List
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n=len(nums)
        if n==1: return True
        inc=-1
        for i in range(1,n):
            if inc==-1:
                if nums[i-1]<nums[i]:
                    inc=True
                elif nums[i-1]>nums[i]:
                    inc=False
            elif inc==True:
                if nums[i-1]>nums[i]:
                    return False
            elif inc==False:
                if nums[i-1]<nums[i]:
                    return False
        return True
    
s=Solution()
print(s.isMonotonic([1,2,2,3]))
print(s.isMonotonic([6,5,4,4]))
print(s.isMonotonic([1,3,2]))