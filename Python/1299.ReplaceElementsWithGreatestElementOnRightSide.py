from typing import List
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans=[-1]
        gt=arr[-1]
        for i in arr[::-1]:
            gt=max(gt,i)
            ans.append(gt)
        ans.reverse()
        return ans[1:]

s=Solution()
print(s.replaceElements([17,18,5,4,6,1]))
print(s.replaceElements([400]))