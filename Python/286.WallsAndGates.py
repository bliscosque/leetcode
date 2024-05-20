from typing import List

from copy import deepcopy
from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        l,c=len(grid),len(grid[0])
        visited=set()
        movl=[0,0,1,-1]
        movc=[1,-1,0,0]

        def bfs(i,j):
            q=deque()
            q.append((i,j,0))
            visited.add((i,j))
            while q:
                #print(q)
                #print(ans)
                ni,nj,pos=q.popleft()
                for im in range(4):
                    nl,nc=ni+movl[im],nj+movc[im]
                    if 0<=nl<l and 0<=nc<c and grid[nl][nc]>0:
                        if (nl,nc) not in visited:
                            grid[nl][nc]=min(grid[nl][nc],pos+1)
                            q.append((nl,nc,pos+1))
                            visited.add((nl,nc))
            


        for i in range(l):
            for j in range(c):
                if grid[i][j]==0: 
                    visited.clear()
                    bfs(i,j)
                    #print(ans)

       
s=Solution()
grid=[[2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]]
print(s.islandsAndTreasure(grid))
print(grid)

#Output: [
#  [3,-1,0,1],
#  [2,2,1,-1],
#  [1,-1,2,-1],
#  [0,-1,3,4]
#]
