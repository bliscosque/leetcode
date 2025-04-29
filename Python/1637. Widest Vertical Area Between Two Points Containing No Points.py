from typing import List
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        pnts_x=[p[0] for p in points]
        pnts_x.sort()
        max_width=0
        for i in range(len(pnts_x)-1):
            max_width=max(max_width,pnts_x[i+1]-pnts_x[i])
        return max_width


s=Solution()
print(s.maxWidthOfVerticalArea([[8,7],[9,9],[7,4],[9,7]])) # 1
print(s.maxWidthOfVerticalArea([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]])) # 3