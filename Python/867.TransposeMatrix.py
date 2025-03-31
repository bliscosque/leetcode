from typing import List
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        L,C=len(matrix),len(matrix[0])
        ans=[[] for _ in range(C)]
        #print(L,C,ans)
        for i in range(L):
            for j in range(C):
                ans[j].append(matrix[i][j])
        return ans

s=Solution()
print(s.transpose(matrix = [[1,2,3],[4,5,6]]))