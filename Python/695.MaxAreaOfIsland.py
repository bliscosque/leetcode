from typing import Optional, List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area=0
        visited=set()
        nl,nc=len(grid),len(grid[0])
        self.area=0

        def inter(l,c):
            visited.add((l,c))
            self.area+=1
            movh=[0,0,1,-1]
            movv=[1,-1,0,0]
            for mov in range(4):
                newl,newc=l+movh[mov],c+movv[mov]
                if 0<=newl<nl and 0<=newc<nc:
                    if grid[newl][newc]==1 and (newl,newc) not in visited:
                        inter(newl,newc)

        
        for l in range(nl):
            for c in range(nc):
                if grid[l][c]==1 and (l,c) not in visited:
                    self.area=0
                    inter(l,c)
                    max_area=max(max_area,self.area)
        
        return max_area


        

s=Solution()
print(s.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])) # 11
print(s.maxAreaOfIsland([[0,0,0,0,0,0,0,0]])) # 0