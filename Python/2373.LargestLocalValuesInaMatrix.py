from typing import List
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        ans=[[0 for _ in range(n-2)] for _ in range(n-2)] 
        for i in range(n-2):
            for j in range(n-2):
                for k in range(3):
                    for l in range(3):
                        ans[i][j]=max(ans[i][j],grid[i+k][j+l])
        return ans

        
s=Solution()
print(s.largestLocal(grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]])) #[[9,9],[8,6]]
print(s.largestLocal(grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]])) #[[2,2,2],[2,2,2],[2,2,2]]