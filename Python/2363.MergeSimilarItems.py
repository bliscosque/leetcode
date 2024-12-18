from typing import List
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        hm={}
        for v,w in items1:
            hm[v]=hm.get(v,0)+w
        for v,w in items2:
            hm[v]=hm.get(v,0)+w
        ans=list(hm.items())
        ans.sort()
        return ans


s=Solution()
print(s.mergeSimilarItems(items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]))