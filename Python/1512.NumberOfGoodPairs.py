from typing import List
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt={}
        for n in nums:
            cnt[n]=1+cnt.get(n,0)
        tot=0
        for v in cnt.values():
            if v>1:
                tot+=(v*(v-1))//2
        return tot

s=Solution()
print(s.numIdenticalPairs([1,2,3,1,1,3])) #4
print(s.numIdenticalPairs([1,1,1,1])) #6
print(s.numIdenticalPairs([1,2,3])) #0