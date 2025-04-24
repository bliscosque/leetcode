from typing import List
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        ans=[]
        for i in range(m):
            ans.append(original[i*n:(i+1)*n])
        return ans

s=Solution()
print(s.construct2DArray([1,2,3,4], 2, 2)) # [[1,2],[3,4]]
print(s.construct2DArray([1,2,3], 1, 3))    # [[1,2,3]] 
print(s.construct2DArray([1,2], 1, 1))       # []