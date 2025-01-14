from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c={}
        for n in nums:
            c[n]=1+c.get(n,0)
        n=len(nums)//3
        ans=[k for k,v in c.items() if v>n]
        return ans
        

s=Solution()
print(s.majorityElement([3,2,3]))