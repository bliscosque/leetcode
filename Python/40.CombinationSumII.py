# TLE!

from typing import Optional, List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans=set()
        def combSumInt(target, pos, path):
            if target==0:
                ans.add(tuple(path))
                return
            for i in range(pos,len(candidates)):
                if i>pos and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                combSumInt(target-candidates[i],i+1,path+[candidates[i]])
               
                    
        combSumInt(target,0,[])
        
        return [list(i) for i in ans]

s=Solution()
print(s.combinationSum2([10,1,2,7,6,1,5],8))
print(s.combinationSum2([1,1,2],2))
print(s.combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],27))