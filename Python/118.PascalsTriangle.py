from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[[1]]
        for i in range(1,numRows):
            l=[1]
            for j in range(i-1):
                l.append(ans[-1][j]+ans[-1][j+1])
            l.append(1)
            ans.append(l.copy())
        return ans
    
s=Solution()
print(s.generate(5))
print(s.generate(1))