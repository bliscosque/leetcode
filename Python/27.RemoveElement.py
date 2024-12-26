from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        s=0
        for e in range(len(nums)):
            if nums[e]!=val:
                nums[s]=nums[e]
                s+=1
        return s



s=Solution()
m=[3,2,2,3]
print(s.removeElement(m, val = 3))
print(m)
m=[0,1,2,2,3,0,4,2]
print(s.removeElement(m, val = 2))
print(m)