from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l=len(matrix)
        for i in range(l):
            for j in range(i+1,l):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(l):
            for j in range(l//2):
                matrix[i][j],matrix[i][l-j-1]=matrix[i][l-j-1],matrix[i][j]
                


s=Solution()
m=[[1,2,3],[4,5,6],[7,8,9]]
s.rotate(m)
print(m)

m2=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
s.rotate(m2)
print(m2) # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]