from typing import List
import math
class Solution:
    def majorityElement_v1(self, nums: List[int]) -> int:
        cnt={}
        maj=(len(nums)+1)//2
        for el in nums:
            cnt[el]=1+cnt.get(el,0)
            if cnt[el]>=maj: return el

    #Bayer-Moore voting system
    def majorityElement(self, nums: List[int]) -> int:
        count=ans=0
        for n in nums:
            if count==0:
                ans=n
            if n==ans:
                count+=1
            else:
                count-=1
        return ans

s=Solution()        
print(s.majorityElement( nums = [3,2,3]))
print(s.majorityElement(nums = [2,2,1,1,1,2,2]))