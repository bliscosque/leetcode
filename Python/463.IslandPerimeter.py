from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        l,c=len(grid),len(grid[0])
        ans=0
        opx=[-1,1,0,0]
        opy=[0,0,1,-1]
        for i in range(l):
            for j in range(c):
                if grid[i][j]==1:
                    for k in range(4):
                        ni,nj=i+opx[k],j+opy[k]
                        if ni<0 or nj<0 or ni>=l or nj>=c:
                            ans+=1
                        elif grid[ni][nj]==0:
                            ans+=1
        return ans 



s=Solution()
print(s.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])) #16
print(s.islandPerimeter([[1]]))#4
print(s.islandPerimeter([[1,0]]))#4