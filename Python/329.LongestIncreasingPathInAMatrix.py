from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        l,c=len(matrix),len(matrix[0])
        dp={}

        def longest_int(i,j):
            
            if (i,j) in dp: return dp[(i,j)]
            movx=[0,0,1,-1]
            movy=[-1,1,0,0]
            ma=0
            for k in range(4):
                ni,nj=i+movx[k],j+movy[k]
                if 0<=ni<l and 0<=nj<c and matrix[ni][nj]>matrix[i][j]:
                    ma=max(ma,longest_int(ni,nj))

            dp[(i,j)]=1+ma
            return dp[(i,j)]
        

        for i in range(l):
            for j in range(c):
                longest_int(i,j)
        
        return max(dp.values())

s=Solution()
print(s.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])) #4
print(s.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]])) #4
print(s.longestIncreasingPath([[1]])) #1