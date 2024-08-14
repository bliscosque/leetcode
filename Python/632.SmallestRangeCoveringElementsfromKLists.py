from typing import List
import math
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n=len(nums)
        cur=[]
        for l in range(n):
            cur.append((nums[l][0],l))
        mindiff=math.inf
        idxs=[0]*n
        arange=[]
        while True:
            cur.sort()
            mi,ma=cur[0][0],cur[-1][0]
            diff=ma-mi
            if mindiff>diff:
                mindiff=diff
                arange=[mi,ma]
            
            miidx=cur[0][1]
            idxs[miidx]+=1
            if idxs[miidx]==len(nums[miidx]):
                break
            cur=cur[1:]+[(nums[miidx][idxs[miidx]],miidx)]

        return arange
        
s=Solution()
print(s.smallestRange(nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]])) # [20,24]
print(s.smallestRange(nums = [[1,2,3],[1,2,3],[1,2,3]])) # [1,1]