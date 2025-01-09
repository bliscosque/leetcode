from typing import List
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        btx=0
        bn=nums[0]
        for x in range(bn,-1,-1):
            while btx<len(nums) and nums[btx]>=x:
                btx+=1
            #print(x,btx)
            if btx==x: return x
        return -1

s=Solution()
print(s.specialArray([3,5])) #2
print(s.specialArray([0,0])) #-1
print(s.specialArray([0,4,3,0,4])) #3