from typing import List
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        ans=0
        for i in range(n):
            ans+=mat[i][i]
            if n-i-1!=i:
                ans+=mat[n-i-1][i]
        return ans
    
s=Solution()
print(s.diagonalSum(mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]))