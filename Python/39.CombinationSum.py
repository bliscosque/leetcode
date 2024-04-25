from typing import Optional, List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans=set()
        def combSumInt(selected,target):
            if target==0:
                poss_ans=selected.copy()
                poss_ans.sort()
                ans.add(tuple(poss_ans))
                return
            if target<0:
                return
            for num in candidates:
                selected.append(num)
                combSumInt(selected,target-num)
                selected.pop()
        combSumInt([],target)
        ansL=[]
        for a in ans:
            ansL.append(list(a))
        return ansL

s=Solution()
print(s.combinationSum([2,3,6,7],7)) # [[2,2,3],[7]]