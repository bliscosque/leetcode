from typing import List
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        l,c=len(grid),len(grid[0])

        # fist, switch lines if 1st digit is 0
        for i in range(l):
            if grid[i][0]==0:
                for j in range(c):
                    grid[i][j]=1 if grid[i][j]==0 else 0 # grid[i][j] ^= 1

        # for each column (staring from second), if it has more 0 than 1, switch
        for j in range(1,c):
            cnt=0
            for i in range(l):
                cnt+=grid[i][j] 

            ## OR: sum(grid[i][j] for i in range(l))
            
            #print(j,cnt)
            if cnt<(l-cnt):
                for i in range(l):
                    grid[i][j]=1 if grid[i][j]==0 else 0

        #print(grid)
        ans=0
        for i in range(l):
            line=0
            for j in range(c):
                line+=2**(c-j-1)*grid[i][j]
            #print(line)
            ans+=line

        return ans
s=Solution()
print(s.matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]])) #0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
print(s.matrixScore([[0]])) #1