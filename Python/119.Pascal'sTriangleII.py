from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans=[1]
        for i in range(rowIndex):
            ans2=[1]
            for j in range(0,len(ans)-1):
                ans2.append(ans[j]+ans[j+1])
            ans2.append(1)
            ans=ans2
        return ans


s=Solution()
print(s.getRow(3))
print(s.getRow(0))
print(s.getRow(1))