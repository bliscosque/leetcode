from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        hm={}
        for i in range(k+1):
            if i<n:
                el=nums[i]
                hm[el]=1+hm.get(el,0)
                if hm[el]>1:
                    return True
        #print(hm)
        for i in range(k+1,n):
            rel=nums[i-k-1]
            hm[rel]-=1

            el=nums[i]
            hm[el]=1+hm.get(el,0)
            if hm[el]>1:
                return True
            
        return False

s=Solution()
print(s.containsNearbyDuplicate(nums = [1,2,3,1], k = 3))
print(s.containsNearbyDuplicate(nums = [1,0,1,1], k = 1))
print(s.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))