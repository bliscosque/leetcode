from fractions import Fraction
from typing import List
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        hm={}
        ans=0
        for rec in rectangles:
            f=Fraction(rec[0],rec[1])
            hm[f]=1+hm.get(f,0)
        for v in hm.values():
            if v>1:
                ans+=((v)*(v-1))//2
        return ans

    
        
s=Solution()
print(s.interchangeableRectangles([[4,8],[3,6],[10,20],[15,30]])) #6
print(s.interchangeableRectangles([[4,5],[7,8]])) # 0