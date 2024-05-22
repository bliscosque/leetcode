from typing import List
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        l,c=len(heights), len(heights[0])
        ans=[]
        canPacific=[[False]*c for _ in range(l)]
        canAtlantic=[[False]*c for _ in range(l)]
        for i in range(c): # first and last line
            canPacific[0][i]=True
            canAtlantic[l-1][i]=True

        for i in range(l): #first and last column
            canPacific[i][0]=True
            canAtlantic[i][c-1]=True

        n_changes=1
        movl=[0,0,1,-1]
        movc=[1,-1,0,0]
        while n_changes:
            n_changes=0
            for i in range(l):
                for j in range(c):
                    for k in range(4):
                        nl,nc=i+movl[k],j+movc[k]
                        if 0<=nl<l and 0<=nc<c:
                            if not canPacific[i][j] and heights[i][j]>=heights[nl][nc] and canPacific[nl][nc]:
                                n_changes+=1
                                canPacific[i][j]=True
                            
                            if not canAtlantic[i][j] and heights[i][j]>=heights[nl][nc] and canAtlantic[nl][nc]:
                                n_changes+=1
                                canAtlantic[i][j]=True
        # ver quais podem os 2 e add no ans, retornar
        for i in range(l):
            for j in range(c):
                if canAtlantic[i][j] and canPacific[i][j]:
                    ans.append([i,j])
        return ans

s=Solution()
print(s.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
print(s.pacificAtlantic([[1]]))
