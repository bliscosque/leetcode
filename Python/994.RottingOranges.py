from typing import List
from copy import deepcopy
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        l,c=len(grid),len(grid[0])
        movl=[0,0,-1,1]
        movc=[1,-1,0,0]
        nfresh=0
        dur=0

        for i in range(l):
            for j in range(c):
                if grid[i][j]==1: 
                    nfresh+=1
        
        if nfresh==0: return 0
        
        while (nfresh>0):
            last_fresh=nfresh
            dur+=1
            ngrid=deepcopy(grid)
            for i in range(l):
                for j in range(c):
                    if grid[i][j]==2: #rotten... go for other
                        for k in range(4):
                            nl,nc=i+movl[k],j+movc[k]
                            if 0<=nl<l and 0<=nc<c:
                                if ngrid[nl][nc]==1: #is fresh...
                                    ngrid[nl][nc]=2
                                    nfresh-=1        
            grid=deepcopy(ngrid)
            #print(grid, nfresh)
            if nfresh==last_fresh: return -1 # impossible
        return dur

        

s=Solution()
print(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])) # 4
print(s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]])) # -1 (impossible)]
print(s.orangesRotting([[0,2]])) # 0 (no fresh)