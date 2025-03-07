from typing import List
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans=0
        inc=set()
        n=len(nums)
        def back(i):
            nonlocal ans,n
            if i==n:
                xor=0
                for el in inc:
                    xor^=nums[el]
                ans+=xor
                return
            back(i+1)
            inc.add(i)
            back(i+1)
            inc.remove(i)
        back(0)
        return ans

s=Solution()
print(s.subsetXORSum([1,3])) #6
print(s.subsetXORSum([5,1,6])) #28
print(s.subsetXORSum([3,4,5,6,7,8])) #480