from typing import List
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        l=len(matrix)
        ans=[]
        for i in range(l):
            mi=min(matrix[i])
            mipos=matrix[i].index(mi)

            valid=True
            for j in range(l):
                if matrix[i][mipos]<matrix[j][mipos]:
                    valid=False
                    break
            if valid:
                ans.append(mi)
        return ans

s=Solution()
print(s.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))
print(s.luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]]))
print(s.luckyNumbers([[7,8],[1,2]]))