from typing import Optional, List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ssTuplesUnique=set()
        def subsetsWithDup_int(parc=[], pos=0):
            #print(parc, pos)
            if pos>=len(nums):
                #print(parc, pos)
                parc.sort()
                ssTuplesUnique.add(tuple(parc))
                return
            subsetsWithDup_int(parc[:],pos+1)
            subsetsWithDup_int(parc[:]+[nums[pos]],pos+1)
        subsetsWithDup_int()
        return [list(t) for t in ssTuplesUnique]



s=Solution()
print(s.subsetsWithDup([1,2,2]))