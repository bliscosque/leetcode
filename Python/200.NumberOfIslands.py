from typing import Optional, List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_l,num_c=len(grid),len(grid[0])
        visited=[[False]*num_c for _ in range(num_l)]
        ans=0
        movl=[1,-1,0,0]
        movc=[0,0,-1,1]

        def bfs(l,c):
            visited[l][c]=True
            for i in range(4):
                nl,nc=l+movl[i],c+movc[i]
                if 0<=nl<num_l and 0<=nc<num_c:
                    # print(grid[nl][nc]," VISITED ",visited[nl][nc])
                    if grid[nl][nc]=="1" and not visited[nl][nc]:
                        # print("here2",nl,nc)
                        bfs(nl,nc)

        for l1 in range(num_l):
            for c1 in range(num_c):
                if grid[l1][c1]=="1" and not visited[l1][c1]:
                    #print(visited)
                    #print("here",l1,c1)
                    ans+=1
                    bfs(l1,c1)


        return ans

            
        

s=Solution()
print(s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])) #1
print(s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])) #2

