from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        i,j=0,0
        ans=0
        n=len(nums)
        spar=0
        while j<n:
            spar+=nums[j]
            j+=1

            #print(i,j,spar)

            if spar==k:
                ans+=1
                
            while spar>=k:
                spar-=nums[i]
                i+=1

        return ans

        

s=Solution()
print(s.subarraySum(nums = [1,1,1], k = 2)) #2
print(s.subarraySum(nums = [1,2,3], k = 3)) #2