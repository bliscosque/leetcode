from typing import List
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        line=[]
        L,C=len(grid),len(grid[0])
        for l in grid:
            line+=l
        k=k%(L*C)
        line=line[-k:]+line[:-k]
        for i in range(L):
            grid[i]=line[i*C:(i+1)*C]
        return grid

s=Solution()
print(s.shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 1)) # [[9,1,2],[3,4,5],[6,7,8]]
print(s.shiftGrid(grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4)) # [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
print(s.shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 9)) # [[1,2,3],[4,5,6],[7,8,9]]
print(s.shiftGrid([[1],[2],[3],[4],[7],[6],[5]],23)) #[[6],[5],[1],[2],[3],[4],[7]]