from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s=set()
        ans=[0]*2
        for n in nums:
            if n in s:
                ans[0]=n
            s.add(n)
        for n in range(1,len(nums)+1):
            if n not in s:
                ans[1]=n
                return ans
            

s=Solution()
print(s.findErrorNums([1,2,2,4])) #[2,3]
print(s.findErrorNums([1,1])) #[1,2]