from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l,c=len(matrix),len(matrix[0])
        lz=set()
        cz=set()
        for i in range(l):
            for j in range(c):
                if matrix[i][j]==0:
                    lz.add(i)
                    cz.add(j)

        for i in range(l):
            for j in range(c):
                if i in lz or j in cz:
                    matrix[i][j]=0
            

s=Solution()
m=[[1,1,1],[1,0,1],[1,1,1]]
s.setZeroes(m)
print(m)

m=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
s.setZeroes(m)
print(m) #[[0,0,0,0],[0,4,5,0],[0,3,1,0]]

m=[[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
s.setZeroes(m)
print(m) #[[0,0,3,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]