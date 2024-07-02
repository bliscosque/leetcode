from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        if n==1: return True
        i=n-2
        searchBig=0
        
        while i>=0:
            #print(i, nums[i],searchBig)
            if searchBig>0:
                if nums[i]>searchBig:
                    searchBig=0
                else:
                    searchBig+=1
            elif nums[i]==0:
                searchBig=1
            i-=1

        return searchBig==0
                
s=Solution()
print(s.canJump([2,3,1,1,4])) # True
print(s.canJump([3,2,1,0,4])) # False
print(s.canJump([4,2,1,0,4])) # True
print(s.canJump([4,2,0,0,4])) # True
print(s.canJump([0])) # True
print(s.canJump([2,0,0])) # True