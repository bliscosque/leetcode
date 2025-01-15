from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_val=nums[0]
        next_pos=1
        cnt=1
        n=len(nums)
        for i in range(1,n):
            if nums[i]!=last_val:
                last_val=nums[i]
                nums[next_pos]=nums[i]
                next_pos+=1
                cnt+=1
        return cnt

s=Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(s.removeDuplicates(nums))
print(nums)
