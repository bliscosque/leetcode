# TLE!

from typing import Optional, List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        used=[False]*len(candidates)
        ans=set()
        def combSumInt(target):
            if target==0:
                ansP=[]
                for i in range(len(candidates)):
                    if used[i]: ansP.append(candidates[i])
                ansP.sort()
                ans.add(tuple(ansP))
                return
            if target<0:
                return
            for i in range(len(candidates)):
                if not used[i]:
                    used[i]=True
                    combSumInt(target-candidates[i])
                    used[i]=False    
        combSumInt(target)
        ansList=[list(i) for i in ans]
        return ansList

s=Solution()
print(s.combinationSum2([10,1,2,7,6,1,5],8))