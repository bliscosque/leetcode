from typing import List
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i,j=0,len(nums)-1
        while i<j:
            while i<j and nums[i]%2==0:
                i+=1
            while i<j and nums[j]%2!=0:
                j-=1
            if i<j:
                nums[i],nums[j]=nums[j],nums[i]
        return nums

s=Solution()
print(s.sortArrayByParity([3,1,2,4]))
print(s.sortArrayByParity([0]))